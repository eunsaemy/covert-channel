#!/usr/bin/env python

###########################################################################################
# FILE
#
#   Name:  main.py
#
#   Developer:  Eunsaem Lee
#
#   Date:       2022-10-17
#
#   Description:
#     This file drives the covert channel application that provides a command line menu to
#     send/receive encrypted data over a covert channel, set Host IP address, and set Key
#     Value to encrypt data.
#
###########################################################################################

import socket
import sys

# Imports Receiver module
import receiver
# Imports Sender module
import sender

HOST_IP = "192.168.0.1"
KEY_VALUE = 3

###########################################################################################
# FUNCTION
#
#   Name:  check_ip
#
#   Parameters:
#     ip        - IP address to send the packets with encrypted data
#
#   Returns:
#     True      - IP address is VALID
#     False     - IP address is INVALID
#     exception - could not connect to IP address
#
#   Description:
#     Determines whether the IP address is valid. If not, prints an error message.
#
###########################################################################################
def check_ip(ip):
    try:
        if ip is None:
            print("IP address is invalid. Please set Host IP address.")
            return False
        else:
            socket.inet_aton(ip)
            return True
    except socket.error:
        print("IP address is invalid. Please set Host IP address.")
        return False

###########################################################################################
# FUNCTION (SETTER)
#
#   Name:  set_ip
#
#   Parameters:
#     None.
#
#   Returns:
#     None.
#
#   Description:
#     Sets the Host IP address. If not, prints an error message.
#
###########################################################################################
def set_ip():
    try:
        global HOST_IP
        HOST_IP = input("Set Host IP: ")
        menu()
    except Exception as error:
        print(str(error))
        menu()

###########################################################################################
# FUNCTION
#
#   Name:  check_key
#
#   Parameters:
#     key       - an integer number from 0 to 25
#
#   Returns:
#     True      - value of key IS an integer from 0 to 25
#     False     - value of key IS NOT an integer from 0 to 25
#     exception - key is not a number; invalid input
#
#   Description:
#     Determines whether the key value is an integer from 0 to 25. If not, prints an
#     error message.
#
###########################################################################################
def check_key(key):
    try:
        if key is None:
            print("Key value is invalid. Please set Key Value to an integer from 0 to 25.")
            return False
        elif 0 <= int(key) <= 25:
            return True
        else:
            print("Key value is invalid. Please set Key Value to an integer from 0 to 25.")
            return False
    except Exception as error:
        print("Key value is invalid. Please set Key Value to an integer from 0 to 25.")
        return False

###########################################################################################
# FUNCTION (SETTER)
#
#   Name:  set_key
#
#   Parameters:
#     None.
#
#   Returns:
#     None.
#
#   Description:
#     Sets the Key Value for Caesar Cipher. If not, prints an error message.
#
###########################################################################################
def set_key():
    try:
        global KEY_VALUE
        KEY_VALUE = int(float(input("Set Key Value: ")))
        menu()
    except Exception as error:
        print(str(error))
        menu()

###########################################################################################
# FUNCTION
#
#   Name:  menu
#
#   Parameters:
#     None.
#
#   Returns:
#     None.
#
#   Description:
#     Provides the user with a command line menu with options to:
#     1. send encrypted data over a covert channel
#     2. receive and decrypt the data
#     3. set Host IP address, and
#     4. set Key Value for Caesar Cipher to encrypt data.
#
###########################################################################################
def menu():
    choice = 0

    print("")
    print("   1. Sender")
    print("   2. Receiver")
    print("   3. Set Host IP Address")
    print("   4. Set Key Value")
    print("   5. Quit")
    print("")

    choice = input("Please choose an option: ")

    print("")

    if choice == "1":
        if check_ip(HOST_IP) and check_key(KEY_VALUE):
            sender.main(HOST_IP, KEY_VALUE)
        else:
            menu()
    elif choice == "2":
        if check_ip(HOST_IP) and check_key(KEY_VALUE):
            receiver.main(KEY_VALUE)
        else:
            menu()
    elif choice == "3":
        set_ip()
    elif choice == "4":
        set_key()
    elif choice == "5":
        print("Goodbye.")
        sys.exit(0)
    else:
        print("Invalid choice. Please try again.")
        menu()

###########################################################################################
# FUNCTION (MAIN)
#
#   Name:  main
#
#   Parameters:
#     None.
#
#   Returns:
#     None.
#
#   Description:
#     Provides the user with a command line menu with options.
#
###########################################################################################
def main():
    menu()

###########################################################################################
# FUNCTION (DRIVER)
#
#   Name:  menu
#
#   Parameters:
#     None.
#
#   Returns:
#     None.
#
#   Description:
#     Calls the main function.
#
###########################################################################################
if __name__ == "__main__":
    main()
