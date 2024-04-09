import socket
import argparse

HOST = 'localhost'  # Use uppercase for constants
DATA_PAYLOAD = 2048
BACKLOG = 5

def echo_server(port):
    """Simple echo server that listens for TCP connections and echoes back received data."""

    try:
        # Create a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Enable address/port reuse
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

            # Bind the socket to the specified port
            server_address = (HOST, port)
            sock.bind(server_address)
            print(f"Starting up echo server on {server_address}")

            # Listen for incoming connections
            sock.listen(BACKLOG)

            while True:
                print("Waiting to receive message from client")
                client, address = sock.accept()  # Accept a connection

                try:
                    while True:
                        data = client.recv(DATA_PAYLOAD)  # Receive data
                        if not data:
                            break  # Break loop if no more data

                        print(f"Received data: {data.decode()}")  # Decode and print
                        client.sendall(data)  # Echo back the data
                        print(f"Sent {len(data)} bytes back to {address}")

                finally:
                    client.close()  # Close the client socket

    except socket.error as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Server Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    args = parser.parse_args()
    port = args.port

    echo_server(port)
