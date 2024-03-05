# This program will encript and decript a message using the Hex table and xor operation

def encript(message, key):
    for i in range(len(message)):
        message[i] = hex(ord(message[i]) ^ key)
    print(message)

def decript(message, key):
    for i in range(len(message)):
        message[i] = chr(int(message[i], 16) ^ key)
    print(message)

message = "Hello, World!"
key = 10

encrypted_message = list(message)  # Make a copy of the original message
encript(encrypted_message, key)

decript(encrypted_message, key)