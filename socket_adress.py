import socket
import sys


def reuse_socket_addr():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Create a TCP socket

    # Get and print the initial SO_REUSEADDR state (optional)
    old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print(f"Old sock state: {old_state}")

    # Enable SO_REUSEADDR to allow immediate reuse of the address
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # Get and print the new SO_REUSEADDR state (optional)
    new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print(f"New sock state: {new_state}")

    local_port = 8282

    # Bind the socket to the address and port
    sock.bind(('', local_port))  # Use the same socket 'sock' for binding
    sock.listen(1)  # Start listening for connections

    print(f"Listening on port {local_port}")

    while True:
        try:
            connection, addr = sock.accept()  # Accept incoming connections
            print(f"Connected by {addr[0]}: {addr[1]}")

            # Handle the connection here (e.g., receive and send data)

        except KeyboardInterrupt:
            break  # Exit gracefully on Ctrl+C

        except socket.error as msg:
            print(f"Socket error: {msg}")

if __name__ == '__main__':
    reuse_socket_addr()
