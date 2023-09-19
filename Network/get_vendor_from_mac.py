import requests


def send_request(mac_address):
    url = "https://api.macvendors.com/"
    response = requests.get(url + mac_address)
    if response.status_code != 200:
        raise Exception("Invalid MAC address")
    return response.content.decode()


if __name__ == "__main__":
    while True:
        mac_addr = input("Enter MAC address of the Host you want the vendor: \n>>")
        try:
            vendor = send_request(mac_addr)
        except Exception as e:
            print(e)
            continue
        mac_vendor = mac_addr[:8] + ":XX:XX:XX"
        print(F"All {mac_vendor} belong to {vendor}")
        input(f"Vendor of {mac_addr} is {vendor}")
        break
