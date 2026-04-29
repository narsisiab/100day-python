import random
stages = [
    '''
    +---+
    |   |
    0   |
   /|\  |
   / \  |
   ==== |
    ''',
    '''
    +---+
    |   |
    0   |
   /|\  |
   /    |
   ==== |
    ''',
    '''
    +---+
    |   |
    0   |
   /|\  |
        |
   ==== |
    ''',
    '''
    +---+
    |   |
    0   |
   /|   |
        |
   ==== |
    ''',
    '''
    +---+
    |   |
    0   |
    |   |
        |
   ==== |
    ''',
    '''
    +---+
    |   |
    0   |
        |
        |
   ==== |
    ''',
    '''
    +---+
    |   |
        |
        |
        |
   ==== |
    '''
]
word_list = ["apple", "camel", "baboon"]
#create a variable called lives to keep track of the number of lives left . set life equal to 6.
lives=6

chosen_word = random.choice(word_list)
print(chosen_word)
placeholder = "" 
word_lengh = len(chosen_word)

for place in range(word_lengh):
    placeholder += " _"
print(placeholder)

gameover = False
correct_letter = []
#if guess is not a letter in chosen_word then reduce lives by 1
#if lives goes down to 0 then the game should end  and print you lose.
#print the art from stages that corresponds to the curent number of lives the user has remaining.
while not gameover:
    guess = input("guess a letter: ").lower()
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
        lives-=1
        if lives==0:
            gameover=True
            print("you lose")
    print(stages[lives])
    print(display)

    if "_" not in display:
        gameover = True
        print("you win")
