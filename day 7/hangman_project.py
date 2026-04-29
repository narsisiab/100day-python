# hangman project
import random
import hangman_art
import hangman_word

print(hangman_art.logo)
lives = 6
chosen_word = random.choice(hangman_word.word_list)
# print(chosen_word)
placeholder = ""
word_lengh = len(chosen_word)

for place in range(word_lengh):
    placeholder += " _"
print(placeholder)

gameover = False
correct_letter = []
while not gameover:
    print(f"************you hav {lives} lives left************")
    guess = input("guess a letter: ").lower()
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
    if guess not in chosen_word:
        print(f"guessed {guess} its not in the word you lose a life")
        lives -= 1
        if lives == 0:
            gameover = True
            print(f"************ it was {chosen_word} you lose************")

    print(hangman_art.stages[lives])
    print(display)

    if "_" not in display:
        gameover = True
        print(f"*************its was {chosen_word} you win*************")
