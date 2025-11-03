# Wi-Fi Password Retriever for Windows
# Lists saved Wi-Fi networks and shows their passwords (if available)

import os

def get_wifi_passwords():
    """
    Retrieves saved Wi-Fi profiles and their passwords on a Windows machine.
    """
    # Get the list of all Wi-Fi profiles
    command = "netsh wlan show profiles"
    profiles_output = os.popen(command).read()

    # Extract profile names
    profile_names = [
        line.split(":", 1)[1].strip()
        for line in profiles_output.splitlines()
        if "All User Profile" in line
    ]

    if not profile_names:
        print("No Wi-Fi profiles found.")
        return

    # Loop through each profile and retrieve its password
    for profile in profile_names:
        profile_info = os.popen(f'netsh wlan show profile name="{profile}" key=clear').read()
        password = None

        for line in profile_info.splitlines():
            if "Key Content" in line:
                password = line.split(":", 1)[1].strip()
                break

        if password:
            print(f"Wi-Fi: {profile}, Password: {password}")
        else:
            print(f"Wi-Fi: {profile}, Password: Not found or protected")

# Run the function
if __name__ == "__main__":
    get_wifi_passwords()
