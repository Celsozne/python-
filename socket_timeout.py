import socket

def test_socket_timeout():
    """
    Tests setting and retrieving the timeout for a socket.
    """

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Corrected socket type
        s.settimeout(100)  # Use settimeout for clarity
        print(f"Current socket timeout: {s.gettimeout()}")
    except socket.error as e:
        print(f"Error creating socket: {e}")
    finally:
        s.close()  # Close the socket even if an error occurs

if __name__ == "__main__":
    test_socket_timeout()
