import socket

send_buf_size = 4096
recv_buf_size = 4096

def modify_buffer_size():
   """
   Modifies the send and receive buffer sizes of a socket.
   """

   try:
       sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

       # Get the initial buffer size
       bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
       print(f"Buffer size before: {bufsize}")

       # Enable TCP_NODELAY
       sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

       # Set send and receive buffer sizes
       sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, send_buf_size)
       sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, recv_buf_size)

       # Get the updated buffer size
       bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
       print(f"Buffer size after: {bufsize}")

   except socket.error as e:
       print(f"Error modifying socket buffer size: {e}")
   finally:
       sock.close()  # Close the socket even if an error occurs

if __name__ == "__main__":
   modify_buffer_size()
