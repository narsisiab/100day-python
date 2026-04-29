# py password generator
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '*', '(', ')', '+']
print("welcome to pypassword generator")

num_letters = int(input("how many letters would yo like in your password?\n"))
num_numbers = int(input("how many numbers would you like in your password?\n"))
num_symbols = int(input("how many symbols do you like in your password?\n"))
password = [""]
for char in range(num_letters):
    password.append(random.choice(letters))

for char in range(num_numbers):
    password.append(random.choice(numbers))

for char in range(num_symbols):
    password.append(random.choice(symbols))

print(password)
fainal_pass = ""

# my logic without help:
# range_num=num_letters+num_numbers+num_symbols
# holder=""
# for i in range(range_num):
#   holder=random.choice(password)
#   fainal_pass += holder
#   password.remove(holder)

# after help:
random.shuffle(password)
for char in password:
    fainal_pass += char

print(fainal_pass)
