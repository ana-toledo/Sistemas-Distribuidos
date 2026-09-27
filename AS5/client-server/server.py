from socket import *
from threading import Thread
from functions import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(("localhost", 5000))
s.listen()
print("Waiting for connection...")
while True: # forever
  (conn, addr) = s.accept() # returns new socket and addr. client
  data = conn.recv(1024) # receive data from client
  print("Received:", data.decode())
  thread = Thread(target=process_request,args=(conn, data))
  thread.start()