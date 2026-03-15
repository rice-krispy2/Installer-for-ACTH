# ACNH Installer
# Created March 14th, 2026
# Created by mitzikritzi2191

# We need to achieve the following:
# 1, Download eden
# 2, Move the appropriate archivos a el correct destination
# 3, Provide any extra features requested.

from pathlib import Path
import os
import requests

home = Path.home()

eden_url = "https://git.eden-emu.dev/eden-emu/eden/releases/download/v0.2.0-rc1/Eden-Windows-v0.2.0-rc1-amd64-msvc-standard.zip"

file_type = {"downloadformat": "zip"}

file_name = f"{home}\Downloads\Eden.zip"

# Print text to the console
print("Hello! Welcome to the official installer for ACNH.")
print("This script will download eden for you and install")
print("the Prod.keys file and Title.keys file for you!")
consent = input("May I download the latest eden version? (As of 15/03/2026 that is v0.2.0-rc1!): ")

def downloadEden(consent):
    if consent == "No" or consent == "no" or consent == "nO" or consent == "NO":
        print("That's okay ^^ I will not download Eden.")
        print("This program will be terminated. Thank you for using it!")
    elif consent == "Yes" or consent == "yes"  or consent == "Si" or consent == "Sí" or consent == "yEs" or consent == "yES" or consent == "YES" or consent == "sí" or consent == "SÍ" or consent == "sÍ" or consent == "si":
        print("Okay! Downloading Eden now...")
        downloaded_file = requests.get(eden_url, params=file_type)
        sanity_check = downloaded_file.ok
        if sanity_check == False:
            print("Download Failed! Please restart the program.")
        elif sanity_check == True:
            print("Download Succeeded! Now saving...")
            with open(file_name, mode="wb") as file:
                file.write(downloaded_file.content)
            print(f"Eden has been downloaded and saved to {file_name}! Now preparing for the next steps in installation!")
downloadEden(consent)
print(f"In phase two of installation, I will be extracting 'Eden.zip' that is located in {file_name}!")
print("I will also be creating a folder called 'user' in the Eden directory, and I will be creating a subdirectory called 'keys' ^^")