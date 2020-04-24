from __future__ import print_function
import logging

import grpc
import sys
import tweet_analyzer_pb2
import tweet_analyzer_pb2_grpc

def convert(s):
    new = ""
    for x in s:
        new += x
    return new

def run(server_ip_port, topic, tweet_count):
    channel = grpc.insecure_channel(server_ip_port)
    stub = tweet_analyzer_pb2_grpc.Tweet_AnalyzerStub(channel)
    response = stub.Tweet_Sentiment_Request(tweet_analyzer_pb2.Tweet_Analyzer_Request(hashtag = topic, num_tweets = tweet_count))
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
    server_ip_port = sys.argv[1:][0]
    topic = sys.argv[1:][1]
    tweet_count = int (sys.argv[1:][2])

    logging.basicConfig()
    run(server_ip_port, topic, tweet_count)
