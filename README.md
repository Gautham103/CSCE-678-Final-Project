# CSCE-678-Final-Project

## Setup

pip3 install grpc_tools, protobuf, grpcio-tools, grpcio

Compile proto file:
```
python3 -m grpc_tools.protoc -I./. --python_out=. --grpc_python_out=. tweet_analyzer.proto
```

## Steps to Run
Run Server:
```
python3 twitter_analyzer_server.py
```

Run Client:
```
python3 twitter_analyzer_client.py
```
