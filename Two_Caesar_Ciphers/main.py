import random


def encrypt(message, key): 
    random_numb = random.randrange(1,1000)
    print("the random number shift is", random_numb)
    for i in message:
        print(chr(ord(i) + key + random_numb), end = "")

def decrypt(message, key, random_numb):
    for i in message:
        print(chr(ord(i) - key - random_numb), end="")


input_message = input("Enter a message to encrypt: ")
input_key = int(input("Enter a key: "))

encrypt(input_message, input_key)

output_message = input("Enter a message to decrypt: ")
output_key = int(input("Enter a key: "))
output_random_numb = int(input("Enter the random number shift: "))

decrypt(output_message, output_key, output_random_numb)
