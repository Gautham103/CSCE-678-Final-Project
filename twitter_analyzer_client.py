from __future__ import print_function
import logging

import grpc

import tweet_analyzer_pb2
import tweet_analyzer_pb2_grpc


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = tweet_analyzer_pb2_grpc.Tweet_AnalyzerStub(channel)
        response = stub.Tweet_Sentiment_Request(tweet_analyzer_pb2.Tweet_Analyzer_Request(hashtag = 'covid19', num_tweets = 100))
    print("Postivie tweets received: " + str(response.pos_tweets))
    print("Negative tweets received: " + str(response.neg_tweets))
    print("Neutral tweets received: " + str(response.neu_tweets))



if __name__ == '__main__':
    logging.basicConfig()
    run()
