import socket

def get_remote_machine_info():
    remote_host = 'g1.globo.com'  # Use the hostname without the protocol
    try:
        print("IP address: %s" % socket.gethostbyname(remote_host))
    except socket.error:
        print("%s error undefined" % (remote_host))

get_remote_machine_info()  # Call the function to execute it
