# rock paper scissur
import random
user_choose = int(
    input("what do you choose? type 0 for rock 1 for paper and 2 for scissurs: "))
computer_choose = random.randint(0, 2)
game = ["rock", "paper", "scissures"]
if user_choose >= 0 and user_choose <= 2:
    print(f" your choose is :{game[user_choose]}")

print(f" the computer choose is :{game[computer_choose]}")

if user_choose > 3 or user_choose < 0:
    print("you typed invalid number you lose!")
elif user_choose == computer_choose:
    print("draw")
elif user_choose == 0 and computer_choose == 2:
    print("you win!")
elif user_choose == 2 and computer_choose == 0:
    print("you lose!")
elif user_choose > computer_choose:
    print("you win")
elif computer_choose > user_choose:
    print("you lose")
