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
------------------------------------------------------------------------------------------------------------------------------
## Modifying the IPs and Running the framework:
In round_robin.py :
1) modify the load balancer grpc server IP and port.
2) modify the self.port to be the same as the port that the proxy servers are running.

In tmp.txt:
1) include IPs of the proxy servers, that are running, separated with comma.

**Run the proxy servers (python3 twitter_analyzer_server.py localhost:<port>)**
  
**Run the load balancers (python round_robin.py)**

In test_client.py:
1) include the IP and port of load balancer grpc server to test_client grpc client channel creation.

**Run the clients (test_client.py)**
