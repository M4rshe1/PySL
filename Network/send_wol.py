import wakeonlan
import re
import os
import json

# check if folder config exists
if not os.path.exists("config"):
    os.mkdir("config")

# chef if file config.json exists
if not os.path.exists("config/config.json"):
    # create file config.json
    with open("config/config.json", "w") as file:
        json.dump([], file)

# MAC address pattern
mac_address_pattern = re.compile("^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$")


# read config.json
def read_json_config():
    with open("config/config.json", "r") as config_file:
        return json.load(config_file)


def write_json_config(json_data):
    with open("config/config.json", "w") as config_file:
        json.dump(json_data, config_file)


def check_mac_address(json_data, mac_addr):
    for mac in json_data:
        # check if object has key name
        if mac.get("mac_address") == mac_addr:
            return True, mac.get("name")
    return False, None


def check_name_address(json_data, given_name):
    for mac in json_data:
        # check if object has key name
        if mac.get("name") == given_name:
            return True, mac.get("mac_address")
    return False, None


def send_wol(mac_addr):
    wakeonlan.send_magic_packet(mac_addr)


# Wake up the computer with the specified MAC address
if __name__ == "__main__":
    while True:
        mac_address = input("Enter MAC address of the Host you want to wake up: \n>>")
        if mac_address_pattern.search(mac_address):
            check, mac_name = check_mac_address(read_json_config(), mac_address)
            if check:
                print("MAC address in config.json")
                print(f"Sending WOL to {mac_name} with MAC address {mac_address}")
                send_wol(mac_address)
                input("Press Enter to exit")
                break
            else:
                print("MAC address not in config.json")
                print("Add MAC address to config.json")
                new_name = input("Enter a name for the MAC address\n>>")
                data = read_json_config()
                data.append({"mac_address": mac_address, "name": new_name})
                write_json_config(data)
                print("MAC address added to config.json")
                send_wol(mac_address)
                input("WOL package sent. Press Enter to exit")
                break
        else:
            check, mac_adr = check_name_address(read_json_config(), mac_address)
            if check:
                print("MAC address in config.json")
                print(f"Sending WOL to {mac_address} with MAC address {mac_adr}")
                send_wol(mac_adr)
                input("Press Enter to exit")
                break
            else:
                print("No MAC address with this name in config.json")
                input("Press Enter to exit")
                break
