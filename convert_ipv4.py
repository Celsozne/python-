import socket
from binascii import hexlify

def get_remote_machine_info():
    """
    Retrieves the IP address of a remote machine.

    Args:
        remote_host: The hostname of the remote machine.

    Returns:
        The IP address of the remote machine as a string.
    """
    remote_host = 'g1.globo.com'  # Use the hostname without the protocol
    try:
        return socket.gethostbyname(remote_host)
    except socket.error:
        print(f"{remote_host} error undefined")
        return None

def ipv4_convert(ip_addr):
    """
    Converts an IPv4 address between packed and unpacked formats.

    Args:
        ip_addr: The IPv4 address to convert, either as a string or the result of get_remote_machine_info().

    Returns:
        None if an error occurs, otherwise a tuple containing the packed and unpacked versions of the IP address.
    """

    try:
        packed_ip = socket.inet_aton(ip_addr)
        unpacked_ip = socket.inet_ntoa(packed_ip)
        print(f"IP address: {ip_addr} => Packed: {hexlify(packed_ip).decode()}, Unpacked: {unpacked_ip}")
    except socket.error as e:
        print(f"Error converting IP address {ip_addr}: {e}")
        return None

if __name__ == "__main__":
    # Get the IP address of the remote machine
    remote_ip = get_remote_machine_info()

    # Convert the IP address if it was successfully retrieved
    if remote_ip:
        ipv4_convert(remote_ip)
