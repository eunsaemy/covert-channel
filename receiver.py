#!/usr/bin/env python

###########################################################################################
# FILE
#
#   Name:  receiver.py
#
#   Developer:  Eunsaem Lee
#
#   Date:       2022-10-17
#
#   Description:
#     This file handles receiving packets, decrypting data using Caesar Cipher, and saving
#     encrypted and decrypted messages into text files.
#
###########################################################################################

# Imports Scapy module
from scapy.all import *

import sys

CHAR = ""
KEY = None

###########################################################################################
# FUNCTION
#
#   Name:  decrypt
#
#   Parameters:
#     enc_data  - encoded data that is being sent in the packet
#     KEY       - Key Value to decrypt data
#
#   Returns:
#     data      - keyboard input
#
#   Description:
#     Creates a packet with a covert message embedded in the packet. If not, prints an
#     error message.
#
###########################################################################################
def decrypt(enc_data, KEY):
    try:
        data = ""

        for i in range(len(enc_data)):
            char = enc_data[i]
            data += chr((ord(char) + 128 - KEY % 128) % 128)

        return data
    except Exception as error:
        print(str(error))

###########################################################################################
# FUNCTION
#
#   Name:  extract_packet
#
#   Parameters:
#     pkt       - TCP packet with an embedded character in its source port
#
#   Returns:
#     None.
#
#   Description:
#     Extracts and decrypts an embedded character in the source port of the TCP packet.
#     Writes the encrypted and decrypted characters into separate text files.
#
###########################################################################################
def extract_packet(pkt):
    global CHAR

    flag = pkt['TCP'].flags

    if flag == 0x40:    # TCP Flag: ECN Echo (ECE)
        CHAR += chr(pkt['TCP'].sport)

        with open('enc_log.txt', 'a') as enc_file:
            enc_file.write(CHAR + " ")

        with open('dec_log.txt', 'a') as dec_file:
            data = decrypt(CHAR, KEY)
            print(data)
            dec_file.write(data + " ")
        CHAR = ""

###########################################################################################
# FUNCTION
#
#   Name:  init
#
#   Parameters:
#     KEY_VALUE - Key Value to decrypt data
#
#   Returns:
#     None.
#
#   Description:
#     Initializes value of Key Value.
#
###########################################################################################
def init(KEY_VALUE):
    global KEY
    KEY = KEY_VALUE

###########################################################################################
# FUNCTION (MAIN)
#
#   Name:  main
#
#   Parameters:
#     KEY_VALUE - Key Value to decrypt data
#
#   Returns:
#     None.
#
#   Description:
#     Initializes value of Key Value for decryption using Caesar Cipher. Uses Scapy to
#     sniff TCP packets and calls the extract packet function. If not, prints an error
#     message.
#
###########################################################################################
def main(KEY_VALUE):
    try:
        init(KEY_VALUE)
        sniff(filter='tcp', prn=extract_packet)
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
