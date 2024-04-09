import socket

host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
print("Host name: %s" %host_name)
print("IP adrress: %s" % ip_address)

