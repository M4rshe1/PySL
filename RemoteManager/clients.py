import tkinter as tk
import subprocess
import json
import os
from paramiko import SSHClient

ssh = SSHClient()

if not os.path.exists(".\cred.json"):
    open("cred.json", "w").close()

# Define your list of clients with their names, IP addresses, usernames, and passwords

JSON_File = open('cred.json')

clients = json.load(JSON_File)

JSON_File.close()


def connect_to_client(client, connection_type):
    print(client)
    ip = client["ip"]
    username = client["username"]
    password = client["password"]
    port = 22
    if "RDP" in connection_type:
        try:
            ps_commands = [
                f'cmdkey /generic:{ip} /user:{username} /pass:{password}',
                f'mstsc /v:{ip}',
                f'cmdkey /delete:TERMSRV/{ip}'
            ]
            for ps_command in ps_commands:
                subprocess.run(['powershell', '-command', ps_command])
        except Exception as e:
            print(f"Error connecting to {client['name']}: {e}")
    elif "SSH" in connection_type:
        # print("SSH")
        # ssh.connect(ip, username=username, password=password)
        cmd = f'plink -ssh {username}@{ip} -pw {password}'
        subprocess.Popen(cmd, shell=True)


app = tk.Tk()
app.title("Remote Manager")
app.geometry("400x250")

# Create a frame for the clients
client_frame = tk.Frame(app)
client_frame.pack(fill=tk.BOTH, expand=True)

# Configure the grid layout with 3 columns
client_frame.grid_rowconfigure(0, weight=1)
client_frame.grid_columnconfigure(0, weight=1)
client_frame.grid_columnconfigure(1, weight=1)
client_frame.grid_columnconfigure(2, weight=1)

# Create buttons for each client
for i, client in enumerate(clients):
    row = i // 3  # Determine the row for the current client
    col = i % 3   # Determine the column for the current client

    client_widget = tk.Frame(client_frame)
    client_widget.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

    title_label = tk.Label(client_widget, text=client["name"])
    title_label.pack(pady=(5, 0))

    for ConTypeBtn in client["buttons"]:
        button = tk.Button(client_widget, text=ConTypeBtn,
                           command=lambda c=client, btn=ConTypeBtn: connect_to_client(c, btn))
        button.pack(pady=5)

app.mainloop()
