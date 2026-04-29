# randomisation and python lists
import random
# random_number=random.randint(1,10)
# print(random_number)
# -------------------------------------------------
# random number between 0-1
# num_0_1=random.random()
# print(num_0_1)
# num_0_10=random.random() *10
# print(num_0_10)
# -------------------------------------------------
# random_float=random.uniform(1,50)
# print(random_float)
# -----------------------------------------------------
# practice : create a head or tails
# my doing:
# random_number=random.random()*20
# if random_number <= 10:
#     print("head")
# else:
#     print("tails")
# can be done this way too:
random_flip = random.randint(0, 1)
if random_flip == 0:
    print("head")
else:
    print("tails")
