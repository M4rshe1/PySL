from datetime import datetime
import os
import nmap
import re

ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
ip_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]{1,2}$")

nm = nmap.PortScanner()


# Print the nmap results
def print_nmap_result(scanned_hosts, ip_address):
    # Check if the folder scans exists
    if not os.path.exists('scans'):
        # If not create the folder
        os.mkdir('scans')
    date_time = datetime.now().strftime("%m.%d.%Y_%H-%M-%S")
    # Write the command run to the file in the scans folder
    open(f'scans/{date_time}.txt', 'w').write("Command Run: " + nm.command_line() + "\n\n\n")
    # Filename is the Date and Time of the scan

    # Print port and version information using the scanned_ports_versions variable
    for port in scanned_hosts['scan'][ip_address]['tcp']:
        port_info = scanned_hosts['scan'][ip_address]['tcp'][port]
        port_state = port_info['state']
        port_name = port_info['name']
        port_product = port_info['product']
        port_version = port_info['version']

        print(f"Port: {port:<5}\tState: {port_state:<10} | "
              f"Name: {port_name:<15}Product: {port_product:<20}Version: {port_version}")

        # Append the port and version information to the file
        open(f'scans/{date_time}.txt', 'a').write(f"Port: {port:<5}\tState: {port_state:<10} | "
                                                  f"Name: {port_name:<15}Product: {port_product:<20}Version: {port_version}\n")
        # close the file
    open(f'scans/{date_time}.txt', 'a').close()


# Scan a specific ip address for open ports and the version of the services that are running on those ports
def nmap_scan_specific_ip():
    while True:
        ip_add_entered = input("\nPlease enter the ip address that you want to scan: \n>> ")
        if ip_add_pattern.search(ip_add_entered):
            print(f"{ip_add_entered} is valid, scanning...")
            break

    try:
        scanned_ports_versions = nm.scan(ip_add_entered, arguments='-p- -sV -sS -O')
        print("Command Run: " + nm.command_line() + " \n")
        print_nmap_result(scanned_ports_versions, ip_add_entered)

    except Exception as e:
        input(e)


def nmap_scan_specific_port():
    while True:
        ip_add_entered = input("\nPlease enter the ip address that you want to scan: \n>> ")
        if ip_add_pattern.search(ip_add_entered):
            print(f"{ip_add_entered} is valid, scanning...  ")
            break

    while True:
        port_error = False
        entered_ports = input("Enter Ports to scan, separated by spaces: \n>> ")
        for port in entered_ports.split():
            if int(port) < 1 or int(port) > 65535:
                print(f"{port} is not a valid port number, Please retry.")
                port_error = True
            # else:
            #     print(f"{port} is a valid port number")
        if not port_error:
            break

    try:
        print(f"Scanning {ip_add_entered} for ports {entered_ports}")
        scanned_ports_versions = nm.scan(ip_add_entered, arguments='-p' + entered_ports + ' -sV -sS -O')
        print("Command Run: " + nm.command_line() + " \n")
        print_nmap_result(scanned_ports_versions, ip_add_entered)
    except Exception as e:
        input(e)


def nmap_scan_discover():
    # scan the network to find the live hosts
    while True:
        ip_range = input("\nPlease enter the ip range you want to scan (ex. 192.168.1.0/24): \n>>")
        if ip_range_pattern.search(ip_range):
            print(f"{ip_range} is a valid, scanning...")
            break
    try:
        nm.scan(hosts=ip_range, arguments='-n -sP -PE -PA21,23,80,3389')
        print("Command Run: " + nm.command_line() + " \n")
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:
            print('{0}:{1}'.format(host, status))
    except Exception as e:
        input(e)


while True:
    print("\nPlease enter the type of scan you want to run.")
    print("IP Port Scanner             [1]")
    print("IP specific Port Scanner    [2]")
    print("Host Discovery              [3]")
    print("Quit                        [4]")
    print("Please enter your choice below: ")
    scan_choice = input(">> ")

    if scan_choice == "1":
        nmap_scan_specific_ip()
    elif scan_choice == "2":
        nmap_scan_specific_port()
    elif scan_choice == "3":
        nmap_scan_discover()
    elif scan_choice == "4":
        break
