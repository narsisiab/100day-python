# lists
# fruits=["apple","cherry","pear"]
# print(fruits[0])
# print(fruits[-1])
# ------------------------------
# editing the list
# fruits=["apple","cherry","pear"]
# print(fruits)
# fruits[1]="cherry1"
# print(fruits)
# --------------------------------
# adding item to end of the list
# fruits=["apple","cherry","pear"]
# fruits.append("banana")
# print(fruits)
# ----------------------------------
# fruits=["apple","cherry","pear"]
# fruits.extend(["banana","orange"])
# print(fruits)
# ---------------------------------------
# nested list
# friends = ["amir", "reza", "ali", "mmd", "jasem"]
# fruits=["apple","cherry","pear"]
# combine_list=[friends,fruits]
# print(combine_list)
# ----------------------------------------
# who will pay  my doing:
import random
friends = ["amir", "reza", "ali", "mmd", "jasem"]
random_pay = random.randint(0, 4)
print(f"the {friends[random_pay]} has to pay xd")
# can be done this way :
print(random.choice(friends))
