import nmap
import re
import pyperclip as pycp

ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")


def get_mac_address(ip_address):
    if not ip_add_pattern.search(ip_address):
        print(f"{ip_address} is not a valid ip address")
        return None
    nm = nmap.PortScanner()
    nm.scan(hosts=ip_address, arguments='-n -sP -PE -PA21,23,80,3389')
    hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    for host, status in hosts_list:
        if status == "up":
            return nm[host]['addresses']['mac']


if __name__ == "__main__":
    while True:
        ipaddress = input("Enter ip address of the Host you want the MAC address: \n>>")
        mac_address = get_mac_address(ipaddress)
        print(f"MAC Address of {ipaddress} is {mac_address}")
        # copy the mac address to clipboard
        pycp.copy(mac_address)
        input("MAC address copied to clipboard, press any key to exit")
        break
