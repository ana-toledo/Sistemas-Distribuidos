from socket import *
from functions import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(("localhost", 5000))
s.listen(1)
print("Waiting for connection...")
(conn, addr) = s.accept() # returns new socket and addr. client
while True: # forever
  data = conn.recv(1024) # receive data from client
  if not data: break # stop if client stopped
  print("Received:", data.decode())
  msg = str(send_params(data.decode())) # process the incoming data into a response
  conn.send(msg.encode()) # return the response
conn.close() # close the connection
s.close()