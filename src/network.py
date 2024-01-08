import socket

import psutil


def get_inferred_default_interface():
    # Getting all network interfaces and their addresses
    net_info = psutil.net_if_addrs()

    # Iterating through interfaces to find the active one
    for interface, addrs in net_info.items():
        for addr in addrs:
            # Checking if the address is an IPv4 address and not a loopback address
            if addr.family == socket.AF_INET and not addr.address.startswith("127."):
                return interface

    # Returning None if no active interface is found
    return None


# When file is executed, it prints the value returned from get_inferred_default_interface()
if __name__ == "__main__":
    active_interface = get_inferred_default_interface()
    print(active_interface)
