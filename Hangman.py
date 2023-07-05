# Import
import random
import Hangman_art
from Hangman_word import word_list

# Printing LOGO By importing. 
print(Hangman_art.logo)

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

lives = 6

display = []
for _ in chosen_word:
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    guess_letter = input("Guess a letter: ").lower()

    if guess_letter in display:
        print(f"You've already guessed {guess_letter}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess_letter :
            display[position] = letter

    if guess_letter not in chosen_word:
        print(f"You guessed {guess_letter}, thats's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            print(f"You lose!. The word was {chosen_word}")
            end_of_game = True
    print(display) 

    print(Hangman_art.stages[lives])
   
    if "_" not in display:
        end_of_game = True
        print ("You win!")
    