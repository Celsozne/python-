import socket

def convert_integer():
   """
   Converts an integer to its network and host byte order representations.
   """

   data = 1234

   print(f"Original: {data}")
   print(f"Long host byte order: {socket.ntohl(data)}")
   print(f"Network byte order: {socket.htonl(data)}")

if __name__ == "__main__":
   convert_integer()
