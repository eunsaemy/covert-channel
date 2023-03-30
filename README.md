## Covert Channel

A covert channel application that:
- reads from the keyboard input and sends the data out over a covert channel
- encrypts sending data using Caesar cipher
- decrypts receiving data using Caesar cipher
- prints out the unencrypted data
- sets host IP address
- sets key value for the Caesar cipher

### Install pynput and Scapy using the commands:

```pip install pynput```
if unable, try running `dnf install python3-devel` first

```pip install scapy```

### To run main.py:

```python main.py```

### Caesar Cipher Algorithm

- [Encrypt and Decrypt Messages using Caesar Cipher](https://www.geeksforgeeks.org/caesar-cipher-in-cryptography/)
- [Encrypt and Decrypt ASCII Codes using Caesar Cipher](https://stackoverflow.com/questions/47685789/caesar-cipher-with-ascii-characters)
