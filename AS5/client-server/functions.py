from random import randint, choice

def send_params(msg):
  params = msg.split()
  if params[0] == "SUM":
    return int(params[1]) + int(params[2])
  elif params[0] == "SUB":
    return int(params[1]) - int(params[2])
  elif params[0] == "MULT":
    return int(params[1]) * int(params[2])
  else:
    return "Invalid Operation."

def process_request(conn, data):
  msg = str(send_params(data.decode()))
  conn.send(msg.encode())
  conn.close()

def generate_request():
    operation = choice(["SUM", "SUB", "MULT"])
    a = randint(1, 100)
    b = randint(1, 100)
    return f"{operation} {a} {b}"
