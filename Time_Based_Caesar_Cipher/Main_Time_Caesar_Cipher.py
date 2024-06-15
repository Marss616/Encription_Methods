# this program will encrypt a message using the Caesar cipher method and a shift key that is generated from the current time

import datetime

def create_shift_key_with_date():
    date = datetime.datetime.now()
    date_split = str(date).split(" ")
    shift = 0  # Initialize shift value
    # sprint("current time: ")
    # print(datetime.datetime.now())
    
    for i, v in enumerate(date_split):
        if i == 1:  # This selects the time part of the date
            for x in v:
                if x.isdigit():  # Check if the character is a digit
                    shift += int(x)  # Convert the digit to an integer and add it to shift
    return shift % 26  # Ensure the shift is within 0-25

def caesar_cipher(text, shift):
    encrypted_text = ""
    
    for char in text:
        if char.isalpha():  # Check if the character is an alphabet
            start = 65 if char.isupper() else 97  # Determine the alphabet start
            encrypted_char = chr((ord(char) + shift - start) % 26 + start)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
            
    return encrypted_text

# Usage example
text = input("What Do you want to encrypt: ")
shift = create_shift_key_with_date()  # Get the shift from the current date and time
time = datetime.datetime.now()
encrypted_text = caesar_cipher(text, shift)

print("current Shift: ", shift)
print("current Encripted text: ", encrypted_text)
print("current Time: ", time)
