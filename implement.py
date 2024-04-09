import socket
from binascii import hexlify

def get_remote_machine_info():
   """
   Retrieves the IP address of a remote machine.

   Args:
       remote_host: The hostname of the remote machine.

   Returns:
       The IP address of the remote machine as a string, or None if an error occurs.
   """
   remote_host = 'eteccamargoaranha.com.br'  # Use the hostname without the protocol
   try:
       return socket.gethostbyname(remote_host)
   except socket.error as e:
       print(f"{remote_host} error undefined: {e}")
       return None

def find_name_service(remote_ip):
   """
   Finds the service names associated with given ports and protocols for a specific IP address.

   Args:
       remote_ip: The IP address of the remote machine.
   """

   for port in [80, 25]:
       protocol = 'tcp'  # Set protocol for each iteration
       try:
           service_name = socket.getservbyport(port, protocol)
           print(f"IP: {remote_ip}, Port: {port} (protocol: {protocol}) => service name: {service_name}")
       except socket.error as e:
           print(f"IP: {remote_ip}, Port {port} (protocol: {protocol}): {e}")

   port = 53
   protocol = 'udp'
   try:
       service_name = socket.getservbyport(port, protocol)
       print(f"IP: {remote_ip}, Port: {port} (protocol: {protocol}) => service name: {service_name}")
   except socket.error as e:
       print(f"IP: {remote_ip}, Port {port} (protocol: {protocol}): {e}")

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
   remote_ip = get_remote_machine_info()

   if remote_ip:
       find_name_service(remote_ip)
ipv4_convert(remote_ip)