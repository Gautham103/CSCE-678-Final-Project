from concurrent import futures
from absl import flags
from absl import app
import grpc
import sys

import tweet_analyzer_pb2
import tweet_analyzer_pb2_grpc
import load_balancer_pb2
import load_balancer_pb2_grpc

import os

flags.DEFINE_integer("num_servers", 2, "Number of Servers in the model")
flags.DEFINE_integer("cap_server", 2, "Capacity of each server in the model")


FLAGS = flags.FLAGS



class proxy:
	def __init__(self,cap,stb):
		#print('\n(Proxy).... ')
		self.capacity = cap
		self.active_req = 0
		self.proxy_stub = stb
		#self.connected_clients = []


class server_services(object):

	def __init__(self):
		#print('\n(Server Services).... ')
		self.proxies = []
		#self.wait_queue_req = []	
		self.current_proxy = 0
		self.wait_queue_clients = {}
		self.wait_queue_req = {}
		#self.processing_client = {}
		self.polling_interval = (FLAGS.num_servers * FLAGS.cap_server)//2
		self.current_load = 0

		self.current_proxy_dict = {} #key:ip, value:stub


		self.port=50053

		updating = self.update_proxies()
		if not updating:
			print('\nThe new proxy list is corrupted. Terminating the program....')
			return updating


	def find_server(self):
		#print('\n(Find Server).... ')
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


	def update_proxies(self):
		#print('\n(Updating Proxy List).... ')
		new_proxy_file = open('tmp.txt', 'rb')
		proxy_list = new_proxy_file.readlines()
		if len(proxy_list)>1:
			return 0
		#print(proxy_list[0].decode('utf-8'))	

		proxy_list = proxy_list[0].decode('utf-8').split(',')
		#print('List of active servers are : ', proxy_list)

		#self.proxies = []	
		self.current_proxy = 0
		addresses = []
		#tmp_list = ['3.23.64.99:50052', '18.220.137.173:50052']
		#for i in range(0,FLAGS.num_servers):
		for i in range(0,len(proxy_list)):
			proxy_server_address = proxy_list[i]+':'+str(self.port)
			addresses.append(proxy_server_address)
			if proxy_server_address not in self.current_proxy_dict: #takes acre of scaling up
				print('The new proxy server is at address {}'.format(proxy_server_address))
				stub_ = tweet_analyzer_pb2_grpc.Tweet_AnalyzerStub(grpc.insecure_channel(proxy_server_address))
				self.proxies.append(proxy(FLAGS.cap_server, stub_))
				self.current_proxy_dict[proxy_server_address]=stub_

		for key in self.current_proxy_dict.keys():
			if key not in addresses: #takes care of scaling down
				print('\n(The server at address {} is terminated for scaling down).... '.format(key))
				del self.current_proxy_dict[key]
				self.proxies.remove(key)
				
		return 1

	def check_poll(self):
		if self.current_load==self.polling_interval:
			self.current_load=0
			updating = self.update_proxies()
			if not updating:
				print('\nThe new proxy list is corrupted. Terminating the program....')
				return updating
		self.current_load+=1
		return 1		

			



class Load_Balancer(load_balancer_pb2_grpc.Load_BalancerServicer):

	def __init__(self):
		#print('\n(Load Balancer class).... ')
		self.server_service = server_services()
		#print('\n(connection tp proxy servers are created)...')
		

	def Tweet_Sentiment_Request(self, request, context):
		#print('\n(Tweet Sentiment Request).... ')
		updating = self.server_service.check_poll()

		#if current_load == polling_interval:
			#updating = self.server_service.update_proxies()

		if not updating:
			#print('\nThe new proxy list is corrupted. Terminating the program....')
			return updating
		else:
			if_success, proxy_id = self.server_service.find_server()
			if if_success:
				chosen_proxy = self.server_service.proxies[proxy_id]
				print('\nChosen server is {}'.format(proxy_id))
				chosen_stub = chosen_proxy.proxy_stub
				if os.environ.get('https_proxy'):
 					del os.environ['https_proxy']
				response_fromproxy = chosen_stub.Tweet_Sentiment_Request(tweet_analyzer_pb2.Tweet_Analyzer_Request(hashtag = request.hashtag, num_tweets = request.num_tweets))
				chosen_proxy.active_req-=1
				return response_fromproxy
			#current_load+=1	

			#elif not if_success:
				#self.server_service.wait_queue_req.append(request)
				#self.server_service.wait_queue_clients[self.server_service.current_proxy] = 

				#self.server_service.wait_queue_clients.append()
				#wait_queue_req.append(req)
				#wait_queue_clients.append(client's ip)	



def serve():
	#print('\n(serve).... ')
	server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
	#print('\n(going to call load balancer and create load balancer grpc server).... ')
	load_balancer_pb2_grpc.add_Load_BalancerServicer_to_server(Load_Balancer(), server)
	#print('\n(adding insecure port for load balancer grpc server).... ')
	server.add_insecure_port('0.0.0.0:50055')
	#server.add_insecure_port(load_balancer_ip_port)
	#print('\n(starting load balancer grpc server).... ')
	server.start()
	server.wait_for_termination()

def main(argv):
	#print('Load Balancer Begins.... (main)')
	#load_balancer_ip_port = sys.argv[1:][0]
	serve()	

	
#def invoke_waiting():
	#if wait_queue_req:
		#req, cli_ip = wait_queue_req.pop(0), wait_queue_clients.pop(0)
		#return req, cli_ip


if __name__ == '__main__':
	#server_ip_port = sys.argv[1:][0]
	app.run(main)
	#logging.basicConfig()
	



	
