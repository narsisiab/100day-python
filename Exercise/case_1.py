# Write a Python code that accepts two integer numbers.
# If the product of the two numbers is less than or equal to 1000,
#  return their product; otherwise, return their sum.

num_1 = int(input("enter your first number: "))
num_2 = int(input("enter your second number: "))
if num_1 * num_2 <= 1000:
    print(num_2*num_1)
else:
    print(num_1+num_2)
