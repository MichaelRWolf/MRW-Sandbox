#!/usr/bin/env python3

import socket
import subprocess

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


def get_hardware_port(interface):
    networksetup_command_and_args = ['networksetup', '-listallhardwareports']
    result = subprocess.run(networksetup_command_and_args, capture_output=True, text=True)

    # Parsing the output to find the corresponding hardware port for the interface
    output_lines = result.stdout.splitlines()
    hardware_port = ""

    for line in output_lines:
        if line.startswith("Hardware Port"):
            hardware_port = line.split(":")[1].strip()
        if line.startswith("Device"):
            current_interface = line.split(":")[1].strip()
            if current_interface == interface:
                return hardware_port

    return "Unknown"


def main():
    interface = get_inferred_default_interface()
    hardware_port = get_hardware_port(interface)
    print(f"Active interface:\n    '{hardware_port}' ({interface})")


if __name__ == "__main__":
    main()
