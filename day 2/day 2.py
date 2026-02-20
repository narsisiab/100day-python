#  today gool : data types , numbers , operation,type conversion ,f-strings

# subscripting
print("hello"[4])
print("hello"[-1])

# string
print("123"+"234")

# integer = whole number
print(123+456)

# large integer
print(123_456_789)
print(123456789)

# float = floating point number
print(3.14)

# boolean
print(True)
print(False)

# type cheking
print(type("hello"))
print(type(123))
print(type(3.1))
print(type(True))

# type conversion
print(int("123") + int("456"))

# basic operator
print(1+2)
print(6-4)
print(4*2)
print(6/3)  # float result
print(6//3)  # int result
print(2**2)

# round
print(round(1.8236))
print(round(1.569, 2))

# f string (insted of converting)
score = 2
height = 1.8
is_winning = True
print(
    f"your score is : {score} and your height is: {height} you are winning is: {is_winning}")
