import sys
import socket
import argparse

def main():
   parser = argparse.ArgumentParser(description='Socket error examples')
   parser.add_argument('--host', action="store", dest="host", type=str, required=True)  # Host should be a string
   parser.add_argument('--port', action="store", dest="port", type=int, required=True)
   parser.add_argument('--file', action="store", dest="file", required=False)

   given_args = parser.parse_args()
   host = given_args.host
   port = given_args.port
   filename = given_args.file

   try:
       with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # Use with block for automatic closure
           try:
               s.connect((host, port))
           except socket.gaierror as e:
               print(f"Address-related errors connecting to server: {e}")
               sys.exit(1)  # Use sys.exit() for proper termination

           try:
               s.sendall(f"GET {filename} HTTP/1.0\r\n\r\n")
           except socket.error as e:
               print(f"Error sending data: {e}")
               sys.exit(1)

           while True:
               try:
                   buf = s.recv(2048)
               except socket.error as e:
                   print(f"Error receiving data: {e}")
                   sys.exit(1)

               if not buf:  # Check for connection closure
                   break

               sys.stdout.write(buf.decode())  # Decode bytes to string for output

   except socket.error as e:
       print(f"Error creating socket: {e}")
       sys.exit(1)

if __name__ == "__main__":
   main()
