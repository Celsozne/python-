import socket
import argparse

HOST = 'localhost'  # Use uppercase for constants

def echo_client(port):
    """Simple echo client that connects to a server and sends a message."""

    try:
        # Create a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            # Connect to the server
            server_address = (HOST, port)
            sock.connect(server_address)
            print(f"Connected to {server_address}")

            # Send message
            message = 'Test message. This will be echoed'
            print(f"Sending: {message}")
            sock.sendall(message.encode())  # Encode before sending

            # Receive response
            amount_received = 0
            amount_expected = len(message)
            while amount_received < amount_expected:
                data = sock.recv(16)
                amount_received += len(data)
                print(f"Received: {data.decode()}")  # Decode before printing

    except socket.error as e:
        print(f"Socket error: {e}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socket Client Example')
    parser.add_argument('--port', action="store", dest="port", type=int, required=True)
    args = parser.parse_args()
    port = args.port

    echo_client(port)
