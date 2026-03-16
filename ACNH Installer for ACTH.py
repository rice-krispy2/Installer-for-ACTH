# ACNH Installer
# Created March 14th, 2026
# Created by mitzikritzi2191

from pathlib import Path
import os
import requests
from zipfile import ZipFile
import shutil

home = Path.home()
downloads_folder = f"{home}\\Downloads"
eden_url = "https://git.eden-emu.dev/eden-emu/eden/releases/download/v0.2.0-rc2/Eden-Windows-v0.2.0-rc2-amd64-msvc-standard.zip"
file_type = {"downloadformat": "zip"}
file_name = f"{home}\\Downloads\\Eden.zip"
extracted_eden = f"{home}\\Downloads\\Eden"
user_dir = f"{extracted_eden}\\user"
keys_dir = f"{user_dir}\\keys"
fw_check = Path(f"{home}\\Downloads\\Firmware.21.0.0.zip")
keys_check = Path(f"{home}\\Downloads\\prod.keys")
fw_install_path = f"{user_dir}\\nand\\system\\contents\\registered"

# Print text to the console
print("Hello! Welcome to the official installer for ACNH.")
print("This script will download eden for you and install")
print("the Prod.keys file and Title.keys file for you!")
consent = input("May I download the latest eden version? (As of 16/03/2026 that is v0.2.0-rc2!): ")

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
print("I will also be creating a folder called 'user' in the Eden directory, and I will be creating a subdirectory called 'keys' ^-^")

def setupEden():
    with ZipFile(file_name, 'r') as zObject:
        zObject.extractall(path=f"{extracted_eden}")
    print(f"Eden has been extracted and is available in {extracted_eden}!")
    print("Now creating directory 'user'!")
    if not os.path.exists(user_dir):
        os.makedirs(user_dir)
    print("'user' directory created!")
    if not os.path.exists(keys_dir):
        os.makedirs(keys_dir)
    print("'keys' directory created!")
    if not os.path.exists(fw_install_path):
        os.makedirs(fw_install_path)
    print("Firmware install path created!")
setupEden()
print(f"Eden has now been installed and is a portable installation! I will be searching your downloads folder for Prod.keys now!")

def keysNfwCheck():
        if keys_check.is_file():
            print(f"Keys found! Currently moving to {keys_dir}!")
        else:
            print(f"Your keys weren't found! Please move your prod.keys file to {downloads_folder} and rerun the program!")
        if fw_check.is_file():
            print("Firmware found! Installation will continue")
        else:
            print(f"Your firmware wasn't found! Please ensure it is named 'Firmware.21.0.0.zip' and ensure that it is in the {downloads_folder} directory!")
            print("and rerun the program!")
keysNfwCheck()
print("I have successfully found your keys and firmware! I will install them now!")

def installKeysNfw():
    print("Installing keys! Please wait a moment...")
    shutil.move(keys_check, f"{keys_dir}\\prod.keys")
    print("Keys installed! Now installing firmware...")
    with ZipFile(fw_check, 'r') as zObject:
        zObject.extractall(path=f"{fw_install_path}")
    print("Firmware installed!")
installKeysNfw()