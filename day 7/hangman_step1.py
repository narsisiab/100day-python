# randomly choose a word from word_list and put it in a variable called chosen-word then print it .
import random
word_list = ["apple", "camel", "baboon"]
chosen_word = random.choice(word_list)
print(chosen_word)
# ask the user to guess a letter and assign their answer to a variable called guess . make guess lowercase
guess = input("guess a letter: ").lower()
# check if the letter the user guessed(guess) is one of the letter in chosen_word print right if it is
# wrong if  it is not
for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")
