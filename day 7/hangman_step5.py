import random
import hangman_art
# update the word list to use the word_list from hangman_word.py
import hangman_word
# or from hangman_word imort world_list then dose not need (hangman_word.word_list) just the (word_list)

# import the logo from hangman_art.py and print it at the start of the game
print(hangman_art.logo)
lives = 6
chosen_word = random.choice(hangman_word.word_list)
print(chosen_word)
placeholder = ""
word_lengh = len(chosen_word)

for place in range(word_lengh):
    placeholder += " _"
print(placeholder)

gameover = False
correct_letter = []
while not gameover:
    # tell the user how many lives has left
    print(f"************you hav {lives} lives left************")
    guess = input("guess a letter: ").lower()
    # if user enterd a letter they already guessed print the letter and let them know
    # we should not debucate a life for this. e.g you have already guessed a .
    if guess in correct_letter:
        print(f"you have already guessed {guess}")

    display = ""
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display += letter
        else:
            display += " _"
# if the letter is not in the chosen_word print out the letter and let them know its not in the word.
# e.g you guessed d its not in the word you lose a life
    if guess not in chosen_word:
        print(f"guessed {guess} its not in the word you lose a life")
        lives -= 1
        if lives == 0:
            gameover = True
            # update the code below and tell user the corect answer
            print(f"************ it was {chosen_word} you lose************")
# update code below to use stage from hangman_art.py
    print(hangman_art.stages[lives])
    print(display)

    if "_" not in display:
        gameover = True
        # update the code below and tell user the corect answer
        print(f"*************its was {chosen_word} you win*************")
