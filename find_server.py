import socket

def find_name_service():
    """
    Finds the service names associated with given ports and protocols.
    """

    for port in [80, 25]:
        protocol = 'tcp'  # Set protocol for each iteration
        try:
            service_name = socket.getservbyport(port, protocol)
            print(f"Port: {port} (protocol: {protocol}) => service name: {service_name}")
        except socket.error as e:
            print(f"Port {port} (protocol: {protocol}): {e}")

    port = 53
    protocol = 'udp'
    try:
        service_name = socket.getservbyport(port, protocol)
        print(f"Port: {port} (protocol: {protocol}) => service name: {service_name}")
    except socket.error as e:
        print(f"Port {port} (protocol: {protocol}): {e}")

if __name__ == "__main__":
    find_name_service()
