import nmap
import re

ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

nm = nmap.PortScanner()

open_ports = []
while True:
    ip_add_entered = input("\nPlease enter the ip address that you want to scan: ")
    if ip_add_pattern.search(ip_add_entered):
        print(f"{ip_add_entered} is a valid ip address")
        break

try:
    result = nm.scan(ip_add_entered, '0-65535')
    nm.command_line()

    print(result)
except Exception as e:
    input(e)
