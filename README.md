# CSCE-678-Final-Project

## Setup

pip3 install grpc_tools, protobuf, grpcio-tools, grpcio

Compile proto file:
```
python3 -m grpc_tools.protoc -I./. --python_out=. --grpc_python_out=. tweet_analyzer.proto
```
Update twitter_analyzer_server.py with the credentials
```
consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
```

## Steps to Run
Run Client with python3 twitter_analyzer_server.py ip:port. For example:
```
python3 twitter_analyzer_server.py localhost:50052
```

Run Client with python3 twitter_analyzer_client.py ip:port tweet_topic tweet_count. For example:
```
python3 twitter_analyzer_client.py localhost:50052 covid19 100
```
