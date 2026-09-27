from socket import *
from threading import Thread
from time import perf_counter
from functions import generate_request

HOST = "localhost"
PORT = 5000
NUM_REQUESTS = 10000

def send_request(msg):
	s = socket(AF_INET, SOCK_STREAM)
	s.connect((HOST, PORT))
	s.send(msg.encode())
	data = s.recv(1024)
	s.close()

threads = []

i_time = perf_counter()

for i in range(NUM_REQUESTS):
	msg = generate_request()
	thread = Thread(
			target=send_request,
			args=(msg,)
	)
	threads.append(thread)
	thread.start()

for thread in threads:
  thread.join()
	
f_time = perf_counter()

total_time = f_time - i_time

print("Número de requisições:", NUM_REQUESTS)
print("Tempo total (s):", total_time)

