from socket import *

HOST = "localhost"
PORT = 5000

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT)) # connect to server (block until accepted)

# ====== SUM =========================
msg = "SUM 20 30" # compose a message
s.send(msg.encode()) # send the message
data = s.recv(1024) # receive the response
print(data.decode()) # print the result
# ====== SUBTRACTION =================
msg = "SUB 15 30" 
s.send(msg.encode())
data = s.recv(1024) 
print(data.decode())
# ======= MULTIPLICATION =============
msg = "MULT 10 10" 
s.send(msg.encode())
data = s.recv(1024) 
print(data.decode())
# ======= INVALID ====================
msg = "DIV 40 4" 
s.send(msg.encode())
data = s.recv(1024) 
print(data.decode())

s.close() # close the connection