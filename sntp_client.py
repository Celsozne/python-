import socket
import struct
import sys
import time

# Define NTP server address and epoch offset
NTP_SERVER = "pool.ntp.org"  # Replace with a preferred server if needed
TIME1970 = 2208988800  # Number of seconds from 1900 to 1970

def sntp_client():
    """Retrieves time from an NTP server and prints it."""

    try:
        # Create a UDP socket
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Send SNTP request
        data = b"\x1b" + 47 * b"\0"  # Use bytes for binary data
        client.sendto(data, (NTP_SERVER, 123))

        # Receive SNTP response
        data, address = client.recvfrom(1024)

        if data:
            print(f"Response received from: {address}")

            # Unpack timestamp from response
            t = struct.unpack('!12I', data)[10]

            # Convert timestamp to Unix time and print
            t -= TIME1970
            print(f"Time = {time.ctime(t)}")

    except socket.error as e:
        print(f"Error: {e}")
   

if __name__ == '__main__':
    sntp_client()
