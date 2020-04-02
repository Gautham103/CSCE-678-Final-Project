from __future__ import print_function
import logging

import grpc

import tweet_analyzer_pb2
import tweet_analyzer_pb2_grpc

def convert(s):
    new = ""
    for x in s:
        new += x
    return new

def run():
    channel = grpc.insecure_channel('localhost:50052')
    stub = tweet_analyzer_pb2_grpc.Tweet_AnalyzerStub(channel)
    response = stub.Tweet_Sentiment_Request(tweet_analyzer_pb2.Tweet_Analyzer_Request(hashtag = 'covid19', num_tweets = 100))
    print("Postivie tweets received: " + str(response.pos_tweets))
    print("Negative tweets received: " + str(response.neg_tweets))
    print("Neutral tweets received: " + str(response.neu_tweets))

    positive_tweets = stub.Get_Positive_Tweets(tweet_analyzer_pb2.Dummy(temp = 1))
    print ("\n########### POSITIVE TWEETS ###########\n")
    for t in positive_tweets:
        print(convert(t.tweets))


    negative_tweets = stub.Get_Negative_Tweets(tweet_analyzer_pb2.Dummy(temp = 1))
    print ("\n########### NEGATIVE TWEETS ###########\n")
    for t in negative_tweets:
        print(convert(t.tweets))

    neutral_tweets = stub.Get_Neutral_Tweets(tweet_analyzer_pb2.Dummy(temp = 1))
    print ("\n########### NEUTRAL TWEETS ###########\n")
    for t in neutral_tweets:
        print(convert(t.tweets))



if __name__ == '__main__':
    logging.basicConfig()
    run()
