from concurrent import futures
from absl import flags
from absl import app
import grpc
import sys

import tweet_analyzer_pb2
import tweet_analyzer_pb2_grpc
import load_balancer_pb2
import load_balancer_pb2_grpc

flags.DEFINE_integer("num_servers", 1, "Number of Servers in the model")
flags.DEFINE_integer("cap_server", 2, "Capacity of each server in the model")


FLAGS = flags.FLAGS
#FLAGS(sys.argv)



class proxy:
	def __init__(self,cap,stb):
		print('\n(Proxy).... ')
		self.capacity = cap
		self.active_req = 0
		self.proxy_stub = stb
		#self.connected_clients = []



class server_services(object):

	def __init__(self):
		print('\n(Server Services).... ')
		self.proxies = []
		#self.wait_queue_req = []	
		self.current_proxy = 0
		#self.wait_queue_clients = {}
		self.processing_client = {}


		tmp=50053

		for i in range(FLAGS.num_servers):
			stub_ = tweet_analyzer_pb2_grpc.Tweet_AnalyzerStub(grpc.insecure_channel('54.184.106.216:'+str(tmp)))
			#tmp+=1
			self.proxies.append(proxy(FLAGS.cap_server, stub_))

	def find_server(self):
		print('\n(Find Server).... ')
		while True:
			server_id = self.current_proxy%FLAGS.num_servers
			server = self.proxies[server_id]

			if server.active_req < server.capacity:
				success = 1
				start_server = 1000000
				server.active_req += 1
				#server.connected_clients.append(client_ip)
				break
			else:
				success = False
				while True:
					if self.proxies[self.current_proxy%FLAGS.num_servers].active_req < self.proxies[self.current_proxy%FLAGS.num_servers].capacity:
						success = True
						break
					self.current_proxy+=1	
				'''
				start_server = current_server+1
				while current_server != start_server:
					if servers[current_server%num_servers].active_req < servers[current_server%num_servers].capacity:
						success = 1
						round_robin = False
						break
					current_server+=1
				if current_server == start_server:
					success = 0
					break
					#wait_queue_req.append(req)
					#wait_queue_clients.append(client's ip)	
					#the above two commands are done in teh Load_Balancer_class
				elif not round_robin:
					break
				'''	
					
		return success, self.current_proxy	
		




class Load_Balancer(load_balancer_pb2_grpc.Load_BalancerServicer):

	def __init__(self):
		print('\n(Load Balancer class).... ')
		self.server_service = server_services()

	def Tweet_Sentiment_Request(self, request, context):
		print('\n(Tweet Sentiment Request).... ')
		if_success, proxy_id = self.server_service.find_server()
		if if_success:
			chosen_proxy = self.server_service.proxies[proxy_id]
			chosen_stub = chosen_proxy.proxy_stub
			response_fromproxy = chosen_stub.Tweet_Sentiment_Request(tweet_analyzer_pb2.Tweet_Analyzer_Request(hashtag = request.hashtag, num_tweets = request.num_tweets))
			return response_fromproxy

		#elif not if_success:
			#self.server_service.wait_queue_req.append(request)
			#self.server_service.wait_queue_clients[self.server_service.current_proxy] = 

			#self.server_service.wait_queue_clients.append()
			#wait_queue_req.append(req)
			#wait_queue_clients.append(client's ip)	



def serve():
	print('\n(serve).... ')
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	load_balancer_pb2_grpc.add_Load_BalancerServicer_to_server(Load_Balancer(), server)
	server.add_insecure_port('[::]:50051')
	server.start()
	server.wait_for_termination()

def main(argv):
	print('Load Balancer Begins.... (main)')
	serve()	

	
#def invoke_waiting():
	#if wait_queue_req:
		#req, cli_ip = wait_queue_req.pop(0), wait_queue_clients.pop(0)
		#return req, cli_ip


if __name__ == '__main__':
	app.run(main)
	#logging.basicConfig()
	



	
