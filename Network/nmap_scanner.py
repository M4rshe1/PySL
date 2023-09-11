from datetime import datetime
import os
import nmap
import json
import re
from get_mac_ad import get_mac_address

ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
ip_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]{1,2}$")

nm = nmap.PortScanner()


# Print the nmap results
def print_nmap_result(scanned_hosts, ip_address):
    # print(scanned_hosts['scan'][ip_address])
    # Check if the folder scans exists
    if not os.path.exists('scans'):
        # If not create the folder
        os.mkdir('scans')
    date_time = datetime.now().strftime("%m.%d.%Y_%H-%M-%S")

    filename = f'scans/NMAP-{date_time}_({ip_address}).txt'

    # Write the command run to the file in the scans folder
    open(filename, 'a').write("Command Run: " + nm.command_line() + "\n\n\n")
    # Filename is the Date and Time of the scan

    # Print the OS information using the scanned_hosts variable
    print(f"Host: {ip_address}\tStatus: {scanned_hosts['scan'][ip_address]['status']['state']}")
    # print mac address if it is found
    if len(scanned_hosts['scan'][ip_address]['addresses']['mac']) > 0:
        print(f"MAC Address: {scanned_hosts['scan'][ip_address]['addresses']['mac']}")
    # print device vendor if it is found
    if len(scanned_hosts['scan'][ip_address]['vendor']) > 0:
        print(
            f"Vendor: {scanned_hosts['scan'][ip_address]['vendor'][scanned_hosts['scan'][ip_address]['addresses']['mac']]}")
    print(f"OS: {scanned_hosts['scan'][ip_address]['osmatch'][0]['name']}")
    print(f"OS Accuracy: {scanned_hosts['scan'][ip_address]['osmatch'][0]['accuracy']}")
    print(f"OS Type: {scanned_hosts['scan'][ip_address]['osmatch'][0]['osclass'][0]['type']}")
    print(f"OS Vendor: {scanned_hosts['scan'][ip_address]['osmatch'][0]['osclass'][0]['vendor']}")
    print(f"OS Family: {scanned_hosts['scan'][ip_address]['osmatch'][0]['osclass'][0]['osfamily']}")
    print(f"OS Generation: {scanned_hosts['scan'][ip_address]['osmatch'][0]['osclass'][0]['osgen']}")
    # print os distribution like ubuntu or arch if it is found
    if len(scanned_hosts['scan'][ip_address]['osmatch'][0]['osclass'][0]['cpe']) > 0:
        print(f"OS Distribution: {scanned_hosts['scan'][ip_address]['osmatch'][0]['osclass'][0]['cpe'][0]}")
    print("-" * 100)
    # Append the OS information to the file
    open(filename, 'a').write(f"Host: {ip_address}\tStatus: {scanned_hosts['scan'][ip_address]['status']['state']}\n")
    if len(scanned_hosts['scan'][ip_address]['addresses']['mac']) > 0:
        open(filename, 'a').write(f"MAC Address: {scanned_hosts['scan'][ip_address]['addresses']['mac']}\n")
    if len(scanned_hosts['scan'][ip_address]['vendor']) > 0:
        open(filename, 'a').write(f"Vendor: {scanned_hosts['scan'][ip_address]['vendor']}\n")
    open(filename, 'a').write(f"OS: {scanned_hosts['scan'][ip_address]['osmatch'][0]['name']}\n")
    open(filename, 'a').write(f"OS Accuracy: {scanned_hosts['scan'][ip_address]['osmatch'][0]['accuracy']}\n")
    open(filename, 'a').write(f"OS Type: {scanned_hosts['scan'][ip_address]['osmatch'][0]['osclass'][0]['type']}\n")
    open(filename, 'a').write(f"OS Vendor: {scanned_hosts['scan'][ip_address]['osmatch'][0]['osclass'][0]['vendor']}\n")
    open(filename, 'a').write(
        f"OS Family: {scanned_hosts['scan'][ip_address]['osmatch'][0]['osclass'][0]['osfamily']}\n")
    open(filename, 'a').write(
        f"OS Generation: {scanned_hosts['scan'][ip_address]['osmatch'][0]['osclass'][0]['osgen']}\n")
    open(filename, 'a').write("-" * 100 + "\n")
    # Print port and version information using the scanned_ports_versions variable
    for port in scanned_hosts['scan'][ip_address]['tcp']:
        port_info = scanned_hosts['scan'][ip_address]['tcp'][port]
        port_state = port_info['state']
        port_name = port_info['name']
        port_product = port_info['product']
        port_version = port_info['version']

        print(f"Port: {port:<5}\tState: {port_state:<10}"
              f"Name: {port_name:<15}Product: {port_product:<30}Version: {port_version}")

        # Append the port and version information to the file
        open(filename, 'a').write(f"Port: {port:<5}\tState: {port_state:<10}"
                                  f"Name: {port_name:<15}Product: {port_product:<30}Version: {port_version}\n")
    # close the file
    open(filename, 'a').close()
    # convert the scnanned_hosts to json and write it to a file
    open(f'scans/NMAP-{date_time}_({ip_address}).json', 'a').write(json.dumps(scanned_hosts, indent=4))


# Scan a specific ip address for open ports and the version of the services that are running on those ports
def nmap_scan_specific_ip():
    while True:
        ip_add_entered = input("\nPlease enter the ip address that you want to scan: \n>> ")
        if ip_add_pattern.search(ip_add_entered):
            print(f"{ip_add_entered} is valid, scanning...")
            print("Know that this scan can take a while...")
            break

    try:
        scanned_ports_versions = nm.scan(ip_add_entered, arguments='-p- -sV -sS -O')
        print("\nCommand Run: " + nm.command_line() + " \n")
        print_nmap_result(scanned_ports_versions, ip_add_entered)

    except Exception as e:
        input(e)


def nmap_scan_specific_port():
    while True:
        ip_add_entered = input("\nPlease enter the ip address that you want to scan: \n>> ")
        if ip_add_pattern.search(ip_add_entered):
            print(f"{ip_add_entered} is valid, scanning...  ")
            print("Know that this scan can take a while...")
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
        print("\nCommand Run: " + nm.command_line() + " \n")
        print_nmap_result(scanned_ports_versions, ip_add_entered)
    except Exception as e:
        input(e)


def nmap_scan_discover():
    # scan the network to find the live hosts
    while True:
        ip_range = input("\nPlease enter the ip range you want to scan (ex. 192.168.1.0/24): \n>>")
        if ip_range_pattern.search(ip_range):
            print(f"{ip_range} is a valid, scanning...")
            print("Know that this scan can take a while depending on the size of the network.")
            print("It could also miss some hosts if they are not configured to respond to ping requests.")
            break
    try:
        nm.scan(hosts=ip_range, arguments='-n -sP -PE -PA21,23,80,3389 -T4 --max-retries 5 --max-scan-delay 5000ms')
        print("\nCommand Run: " + nm.command_line() + " \n")
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:
            print('{0}:{1}'.format(host, status))
    except Exception as e:
        input(e)


def run_custom_flags():
    while True:
        ip_add_entered = input("Enter IP address or range to scan: \n>> ")
        if not ip_add_pattern.search(ip_add_entered):
            print(f"{ip_add_entered} is valid, scanning...")
            break
    arguments_entered = input("Enter the flags you want to run: \n>> ")
    try:
        scanned_results = nm.scan(ip_add_entered, arguments=arguments_entered)
        print("\nCommand Run: " + nm.command_line() + " \n")
        open(f'scans/NMAP-CUSTOM_({ip_add_entered}).json', 'a').write(json.dumps(scanned_results, indent=4))
    except Exception as e:
        input(e)


while True:
    print("\nPlease enter the type of scan you want to run.")
    print("IP Port Scanner             [1]")
    print("IP specific Port Scanner    [2]")
    print("Host Discovery              [3]")
    print("Get MAC from IP             [4]")
    print("Run NMAP with custom Flags  [5]")
    print("Quit                        [6]")
    print("Please enter your choice below: ")
    scan_choice = input(">> ")

    if scan_choice == "1":
        nmap_scan_specific_ip()
    elif scan_choice == "2":
        nmap_scan_specific_port()
    elif scan_choice == "3":
        nmap_scan_discover()
    elif scan_choice == "4":
        while True:
            ip_addr = input("\nPlease enter the ip address that you want to get the MAC address from: \n>> ")
            if ip_add_pattern.search(ip_addr):
                print(f"{ip_addr} is valid, getting MAC address...")
                break
        get_mac_address(input("Please enter the IP address you want to get the MAC address from: \n>> "))
    elif scan_choice == "5":
        run_custom_flags()
    elif scan_choice == "6":
        break
