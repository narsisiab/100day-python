# conditional statements , logical operators , code blocks and scope

# if / else
# score = int(input("what is your score?"))
# if score >=12:
# print("you pass")
# else:
#   print("you fail")

# modulo operator %
# cheking odd or even
# number = int(input("enter your number to check:"))
# if number%2==0:
# print("even")
# else:
# print("odd")

# nested if/else/elif

print("welcome to the rollercoaster!")
height = int(input("what is your height in cm?"))
bill = 0
if height >= 120:
    print("you can ride")
    age = int(input("how old are you?"))
    if age <= 12:
        print("your ticket is 5$")
        bill = 5
    elif age <= 18:
        print("your ticket is 7$")
        bill = 7
    else:
        print("your ticket is 12$")
        bill = 12
    photo = input("do you want a photo y for yes and n for no: ")
    if photo == "y":
        bill += 3
    print(f"your final bill is {bill}")
else:
    print("your cant ride")
