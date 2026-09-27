from socket import *
from functions import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(("localhost", 5000))
s.listen()
print("Waiting for connection...")
while True: # forever
  (conn, addr) = s.accept() # returns new socket and addr. client
  data = conn.recv(1024) # receive data from client
  if not data: break # stop if client stopped
  msg = str(send_params(data.decode())) # process the incoming data into a response
  conn.send(msg.encode()) # return the response
  conn.close() # close the connection
