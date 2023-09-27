import tkinter as tk
from tkinter import messagebox
import subprocess


def open_client_page():
    main_frame.pack_forget()  # Hide the main page
    client_frame.pack()  # Show the client page


def open_main_page():
    client_frame.pack_forget()  # Hide the client page
    main_frame.pack()  # Show the main page


def clear_placeholder(event):
    if event.widget.get() == event.widget.placeholder:
        event.widget.delete(0, tk.END)
        event.widget.config(fg='black')


def restore_placeholder(event):
    if not event.widget.get():
        event.widget.insert(0, event.widget.placeholder)
        event.widget.config(fg='grey')


def toggle_password_visibility():
    if entry_password.cget('show') == '*':
        entry_password.config(show='')
        show_password_button.config(text='Hide Password')
    else:
        entry_password.config(show='*')
        show_password_button.config(text='Show Password')


def start_rdp(ip, username, password):
    try:
        ps_commands = [
            f'cmdkey /generic:{ip} /user:{username} /pass:{password}',
            f'mstsc /v:{ip}',
            f'cmdkey /delete:TERMSRV/{ip}'
        ]
        for ps_command in ps_commands:
            subprocess.run(['powershell', '-command', ps_command])
    except Exception as e:
        messagebox.showerror("Error", f"RDP session could not be started: {e}")


def on_server_click():
    ip = "192.168.1.225"
    username = "colin"
    password = "Mine2007_?"
    start_rdp(ip, username, password)


def on_client_click():
    open_client_page()


def on_connect_click():
    ip = "192.168.1.225"
    username = entry_username.get()
    password = entry_password.get()
    start_rdp(ip, username, password)


def on_connect_enter(event):
    on_connect_click()


app = tk.Tk()
app.title("RDP Session")
app.geometry("300x200")

main_frame = tk.Frame(app)
main_frame.pack()

server_button = tk.Button(main_frame, text="Server", command=on_server_click)
server_button.pack(pady=20)

client_button = tk.Button(main_frame, text="Client", command=on_client_click)
client_button.pack(pady=20)

client_frame = tk.Frame(app)

client_label = tk.Label(client_frame, text="Client")
client_label.pack()

entry_username = tk.Entry(client_frame, width=20, fg='grey')
entry_username.placeholder = "Username"
entry_username.insert(0, entry_username.placeholder)
entry_username.bind("<FocusIn>", clear_placeholder)
entry_username.bind("<FocusOut>", restore_placeholder)
entry_username.pack()

entry_password = tk.Entry(client_frame, width=20, show="*", fg='grey')
entry_password.placeholder = "Password"
entry_password.insert(0, entry_password.placeholder)
entry_password.bind("<FocusIn>", clear_placeholder)
entry_password.bind("<FocusOut>", restore_placeholder)
entry_password.pack()

show_password_button = tk.Button(client_frame, text="Show Password", command=toggle_password_visibility)
show_password_button.pack(pady=5)

connect_button = tk.Button(client_frame, text="Connect", command=on_connect_click)
connect_button.pack(pady=10)

back_button = tk.Button(client_frame, text="Back", command=open_main_page)
back_button.pack(pady=10)

entry_password.bind("<Return>", on_connect_enter)

app.mainloop()
