from __future__ import print_function
import logging

import load_balancer_pb2
import load_balancer_pb2_grpc

import grpc

def run():
	print('\n(run).... ')
	channel = grpc.insecure_channel('34.209.199.236:50051')
	stub = load_balancer_pb2_grpc.Load_BalancerStub(channel)
	print('\n(going to call tweet sentiment request).... ')
	response = stub.Tweet_Sentiment_Request(load_balancer_pb2.Tweet_Analyzer_Request(hashtag = 'covid19', num_tweets = 100))
	print('\n(tweet sentiment request received).... ')
	print("Postivie tweets received: " + str(response.pos_tweets))
	print("Negative tweets received: " + str(response.neg_tweets))
	print("Neutral tweets received: " + str(response.neu_tweets))

	'''

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
	'''    


if __name__ == '__main__':
	logging.basicConfig()
	run()
