import random
word_list = ["apple", "camel", "baboon"]
chosen_word = random.choice(word_list)
print(chosen_word)
# create a placeholder with the same number of blanlks as chosen_word  _
placeholder = ""
# this work too:
# word_lengh=len(chosen_word)
# for place in range(world_lengh)
for place in chosen_word:
    placeholder += " _"
print(placeholder)
# create a display that puts the guess letter in the right position and _ in the rest of the string.
guess = input("guess a letter: ").lower()
display = ""
for letter in chosen_word:
    if letter == guess:
        display += guess
    else:
        display += "_"
print(display)
