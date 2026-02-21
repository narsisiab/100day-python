print("welcome to pizza deliveries")
bill=0
size=input("what size do you want? s , m or l: ")
if size=="s":
    bill+=15
elif size=="m":
    bill+=20
elif size=="l":
    bill+=25        
pepperoni=input("do you want pepproni on your pizza? y or n: ")
if pepperoni=="y":
    if size=="s":
        bill+=2
    else :
        bill+=3   
extra_cheese=input("do you want extra cheese? y or n: ")
if extra_cheese=="y":
    bill+=1
print(f"your total bill is {bill}$")    
