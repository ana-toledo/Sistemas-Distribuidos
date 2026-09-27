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

