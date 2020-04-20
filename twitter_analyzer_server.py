from concurrent import futures
import logging

import grpc

import tweet_analyzer_pb2
import tweet_analyzer_pb2_grpc

import re
import tweepy
from tweepy import OAuthHandler
from textblob import TextBlob

class TwitterClient(object):
    '''
    Generic Twitter Class for sentiment analysis.
    '''
    def __init__(self):
        '''
        Class constructor or initialization method.
        '''
        # keys and tokens from the Twitter Dev Console
        consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
        access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

        # attempt authentication
        try:
            # create OAuthHandler object
            self.auth = OAuthHandler(consumer_key, consumer_secret)
            # set access token and secret
            self.auth.set_access_token(access_token, access_token_secret)
            # create tweepy API object to fetch tweets
            self.api = tweepy.API(self.auth)
        except:
            print("Error: Authentication Failed")

    def clean_tweet(self, tweet):
        '''
        Utility function to clean tweet text by removing links, special characters
        using simple regex statements.
        '''
        return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())

    def get_tweet_sentiment(self, tweet):
        '''
        Utility function to classify sentiment of passed tweet
        using textblob's sentiment method
        '''
        # create TextBlob object of passed tweet text
        analysis = TextBlob(self.clean_tweet(tweet))
        # set sentiment
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'neutral'
        else:
            return 'negative'

    def get_tweets(self, query, count = 10):
        '''
        Main function to fetch tweets and parse them.
        '''
        # empty list to store parsed tweets
        tweets = []

        try:
            # call twitter api to fetch tweets
            fetched_tweets = self.api.search(q = query, count = count)

            # parsing tweets one by one
            for tweet in fetched_tweets:
                # empty dictionary to store required params of a tweet
                parsed_tweet = {}

                # saving text of tweet
                parsed_tweet['text'] = tweet.text
                # saving sentiment of tweet
                parsed_tweet['sentiment'] = self.get_tweet_sentiment(tweet.text)

                # appending parsed tweet to tweets list
                if tweet.retweet_count > 0:
                    # if tweet has retweets, ensure that it is appended only once
                    if parsed_tweet not in tweets:
                        tweets.append(parsed_tweet)
                else:
                    tweets.append(parsed_tweet)

            # return parsed tweets
            return tweets

        except tweepy.TweepError as e:
            # print error (if any)
            print("Error : " + str(e))


class Tweet_Analyzer(tweet_analyzer_pb2_grpc.Tweet_AnalyzerServicer):


    def Tweet_Sentiment_Request(self, request, context):

        api = TwitterClient()
        tweets = api.get_tweets(query = request.hashtag, count = request.num_tweets)

        self.ptweets = [tweet for tweet in tweets if tweet['sentiment'] == 'positive']
        self.ntweets = [tweet for tweet in tweets if tweet['sentiment'] == 'negative']
        self.neutraltweets = [tweet for tweet in tweets if tweet['sentiment'] == 'neutral']

        postive_tweet_percent = 100*len(self.ptweets)/len(tweets)
        negative_tweet_percent = 100*len(self.ntweets)/len(tweets)
        neutral_tweet_percent = 100 - postive_tweet_percent - negative_tweet_percent

        return tweet_analyzer_pb2.Tweet_Analyzer_Reply(pos_tweets=postive_tweet_percent, neg_tweets=negative_tweet_percent, neu_tweets=neutral_tweet_percent)

    def Get_Positive_Tweets(self, request, context):
        for t in self.ptweets[:5]:
            yield tweet_analyzer_pb2.Tweets(tweets = t['text'])


    def Get_Negative_Tweets(self, request, context):
        for t in self.ntweets[:5]:
            yield tweet_analyzer_pb2.Tweets(tweets = t['text'])

    def Get_Neutral_Tweets(self, request, context):
        for t in self.neutraltweets[:5]:
            yield tweet_analyzer_pb2.Tweets(tweets = t['text'])


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    tweet_analyzer_pb2_grpc.add_Tweet_AnalyzerServicer_to_server(Tweet_Analyzer(), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
