import random
word_list = ["apple", "camel", "baboon"]
chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = ""
word_lengh = len(chosen_word)
for place in range(word_lengh):
    placeholder += " _"
print(placeholder)
# use a while loop to let user guess again
gameover=False
correct_letter=[]
while not gameover:
    guess = input("guess a letter: ").lower()
    display = ""
    # change the for loop so that you keep the previous correct letter in display.
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display+=letter
        else:
            display += "_"
    print(display)

    if "_" not in display:
        gameover=True
        print("you win")
