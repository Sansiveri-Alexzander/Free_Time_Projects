'''
Program to generate a random string of characters
length defined by user
'''

import random

# Define the list of characters to pull password from

'''
*******figure out how to print paranthesis and math equations******
'''

lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
         'm', 'o', 'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
sym = ['!', '@', '#', '$', '%', '^', '&', '*',
       ')', '(', '-', '_', '=', '+', '<', '.', '>', '/', '?']
all_Characters = lower + upper + num + sym


print("Welcome to the Password Generator.")
length = int(input("How long do you want your password to be? (8-30)"))


while length < 8:
    length = int(input('That password is not long enough to be secure. \
Please make it at least 8 characters long. \nTry Again. \
How many characters do you want your password to be? '))
while length > 30:
    length = int(input("That password is too long to be accepted in most \
places.  Please make it less than 30 characters long. \nTry again. How many \
characters would you like your passowrd to be? "))

# Generate 1 of each value, then 26 other random values

password = []

password.append(random.choice(lower))
password.append(random.choice(upper))
password.append(random.choice(num))
password.append(random.choice(sym))

for n in range(length - 4):
    password.append(random.choice(all_Characters))

# Place all characters in a list, that list is the password

random.shuffle(password)

# Print only the required number of characters

print("Your password is: ")
print(''.join(password))
