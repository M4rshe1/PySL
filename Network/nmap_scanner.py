from datetime import datetime
import os
import nmap
import json
import re
from get_mac_ad import get_mac_address
from time import perf_counter
import pyperclip as pycp
from get_vendor_from_mac import send_request as get_vendor

ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
ip_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]{1,2}$")

nm = nmap.PortScanner()


# Print the nmap results
def print_nmap_result(scanned_hosts, ip_address, time_took):
    # print(scanned_hosts['scan'][ip_address])
    # Check if the folder scans exists
    print("\n" * 100)
    if not os.path.exists('scans'):
        # If not create the folder
        os.mkdir('scans')
    date_time = datetime.now().strftime("%m.%d.%Y_%H-%M-%S")
    filename = f'scans/NMAP-{date_time}_({ip_address}).txt'

    # Write the command run to the file in the scans folder
    open(filename, 'a').write("Command Run: " + nm.command_line() + "\n")
    open(filename, 'a').write(f"in {time_took:.2f} seconds" + "\n\n\n")
    print(f"in {time_took:.2f} seconds\n")
    # Filename is the Date and Time of the scan

    # Print the OS information using the scanned_hosts variable
    # print hostname if it is found
    print(f"Host: {ip_address}\tStatus: {scanned_hosts['scan'][ip_address]['status']['state']}")
    # convert time in sec to uptime in d h m s format
    if scanned_hosts.get('scan').get(ip_address).get('seconds'):
        uptime = (
            f"Uptime: {int(scanned_hosts.get('scan').get(ip_address).get('seconds')) // 86400}d "
            f"{int(scanned_hosts.get('scan').get(ip_address).get('seconds')) // 3600 % 24}h "
            f"{int(scanned_hosts.get('scan').get(ip_address).get('seconds')) // 60 % 60}m "
            f"{int(scanned_hosts.get('scan').get(ip_address).get('seconds')) % 60}s "
        )
        print(uptime)
    else:  # if uptime is not found
        uptime = "Uptime: Not Found"
        print(uptime)
    # print mac address if it is found
    if len(scanned_hosts['scan'][ip_address]['hostnames']) > 0:
        print(f"Hostname: {scanned_hosts['scan'][ip_address]['hostnames'][0]['name']}")
    if len(scanned_hosts.get('scan').get(ip_address).get('addresses').get('mac')) > 0:
        print(f"MAC Address: {scanned_hosts.get('scan').get(ip_address).get('addresses').get('mac')}")
    # print device vendor if it is found
    if len(scanned_hosts['scan'][ip_address]['vendor']) > 0:
        print(
            f"Vendor: {scanned_hosts['scan'][ip_address]['vendor'][scanned_hosts.get('scan').get(ip_address).get('addresses').get('mac')]}"
        )
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
    open(filename, 'a').write(uptime + "\n")
    if len(scanned_hosts['scan'][ip_address]['hostnames']) > 0:
        open(filename, 'a').write(f"Hostname: {scanned_hosts['scan'][ip_address]['hostnames'][0]['name']}\n")
    if len(scanned_hosts.get('scan').get(ip_address).get('addresses').get('mac')) > 0:
        open(filename, 'a').write(
            f"MAC Address: {scanned_hosts.get('scan').get(ip_address).get('addresses').get('mac')}\n")
    if len(scanned_hosts['scan'][ip_address]['vendor']) > 0:
        open(filename, 'a').write(
            f"Vendor: {scanned_hosts['scan'][ip_address]['vendor'][scanned_hosts.get('scan').get(ip_address).get('addresses').get('mac')]}\n"
        )
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
        # convert the scanned_hosts to json and write it to a file
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
        # add timer to see how long the scan takes
        start = perf_counter()
        scanned_ports_versions = nm.scan(ip_add_entered, arguments='-p- -sV -sS -O')
        end = perf_counter()
        print("\nCommand Run: " + nm.command_line() + " \n")
        print_nmap_result(scanned_ports_versions, ip_add_entered, end - start)

    except Exception as ex:
        input(ex)


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
        start = perf_counter()
        scanned_ports_versions = nm.scan(ip_add_entered, arguments='-p' + entered_ports + ' -sV -sS -O')
        end = perf_counter()
        print("\nCommand Run: " + nm.command_line() + " \n")
        print_nmap_result(scanned_ports_versions, ip_add_entered, end - start)
    except Exception as ex:
        input(ex)


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
        start = perf_counter()
        nm.scan(hosts=ip_range, arguments='-n -sP -PE -PA21,23,80,3389 -T4 --max-retries 5 --max-scan-delay 5000ms')
        end = perf_counter()
        print("\nCommand Run: " + nm.command_line() + " \n")
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        for host, status in hosts_list:
            print(f"Total time to scan: {end - start:.2f} seconds")
            print('{0}:{1}'.format(host, status))
    except Exception as ex:
        input(ex)


def run_custom_flags():
    while True:
        ip_add_entered = input("Enter IP address or range to scan: \n>> ")
        if not ip_add_pattern.search(ip_add_entered):
            print(f"{ip_add_entered} is valid, scanning...")
            break
    arguments_entered = input("Enter the flags you want to run: \n>> ")
    try:
        start = perf_counter()
        scanned_results = nm.scan(ip_add_entered, arguments=arguments_entered)
        end = perf_counter()
        print("\nCommand Run: " + nm.command_line() + " \n")
        print(f"Total time to scan: {end - start:.2f} seconds")
        open(f'scans/NMAP-CUSTOM_({ip_add_entered}).json', 'a').write(json.dumps(scanned_results, indent=4))
        print("The results have been saved to a file in the scans folder.")
    except Exception as ex:
        input(ex)


while True:
    print("\n" * 100)
    # print("\nPlease enter the type of scan you want to run.")
    print("--------- NMAP Scanner ---------")
    print("IP Port Scanner             [1]")
    print("IP specific Port Scanner    [2]")
    print("Host Discovery              [3]")
    print("Run NMAP with custom Flags  [4]")
    print("--------- MAC Scanner ----------")
    print("Get MAC from IP             [5]")
    print("Get Vendor from MAC         [6]")
    print("------------- Quit -------------")
    print("Quit                        [q]")
    print("Please enter your choice below: ")
    scan_choice = input(">> ")

    if scan_choice == "1":
        nmap_scan_specific_ip()
        input("Press any key to continue...")
    elif scan_choice == "2":
        nmap_scan_specific_port()
    elif scan_choice == "3":
        nmap_scan_discover()
    elif scan_choice == "5":
        while True:
            ip_addr = input("Please enter the IP address you want to get the MAC address from: \n>> ")
            if ip_add_pattern.search(ip_addr):
                print(f"{ip_addr} is valid, getting MAC address...")
                mac_addr = get_mac_address(ip_addr)
                input(f"MAC Address of {ip_addr} is {mac_addr}")
                # copy the mac address to clipboard
                pycp.copy(mac_addr)
                break
            else:
                print(f"{ip_addr} is not a valid IP address, please retry.")
    elif scan_choice == "6":
        while True:
            mac_addr = input("Enter MAC address of the Host you want the vendor: \n>> ")
            try:
                vendor = get_vendor(mac_addr)
            except Exception as e:
                print(e)
                continue
            mac_vendor = mac_addr[:8] + ":XX:XX:XX"
            print(F"All {mac_vendor} belong to {vendor}")
            input(f"Vendor of {mac_addr} is {vendor}")
            break
    elif scan_choice == "4":
        run_custom_flags()
    elif scan_choice == "q":
        break
