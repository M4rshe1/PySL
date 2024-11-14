import os
import subprocess
import csv


def export_profiles(mode):
    key_word = ""
    language = (subprocess.check_output(["Get-WinSystemLocale", "|", "convertTo-Json", "-depth", "5"])
                .decode('utf-8', errors='ignore'))
    print(language)

    # Get all Wi-Fi profiles
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors='ignore').split('\n')
    profile_names = [line.split(':')[1].strip() for line in data if " : " in line]

    filename = subprocess.check_output(['hostname']).decode('utf-8',
                                                            errors='ignore').strip() + "-wifi-passwords.csv"

    # delete file if it exists
    if os.path.exists("./scans/" + filename):
        os.remove("./scans/" + filename)
    print("---------------------------------------")
    # Iterate through the profiles and retrieve their passwords

    with open("./scans/" + filename, "w", newline="") as csvfile:
        fieldnames = ['profile', 'password']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
        writer.writeheader()

    for profile_name in profile_names:
        # print(profile_name)
        try:
            # Get the Wi-Fi profile details, including the password
            profile_info = subprocess.check_output(
                ['netsh', 'wlan', 'show', 'profile', profile_name, 'key=clear']).decode(
                'utf-8', errors='ignore')
            # Search for the password in the profile details
            password_line = [line for line in profile_info.split('\n') if key_word in line]

            if password_line:
                password = password_line[0].split(":")[1].strip()

                print(f"Profile   :  {profile_name}")
                print(f"Password  :  {password}")
                print("---------------------------------------")

                writer.writerow({'profile': profile_name, 'password': password})

        except subprocess.CalledProcessError as e:
            print(f"Error retrieving password for profile {profile_name}: {e}")


if __name__ == '__main__':
    export_profiles(input("System-language: English (e) or German (g)?\n>> ").lower())
