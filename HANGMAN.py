import random

wordList = [
"pink", "blue", "yellow", "maroon", "purple", "green", "cyan", "fuschia",
 "gray", "white", "black", "teal", "neon", "orange", "babypink"
           ]

guess_word = []
secretWord = random.choice(wordList) 
length_word = len(secretWord)
alphabet = "abcdefghijklmnopqrstuvwxyz"
letter_storage = []



def beginning():
    print("Hi! Welcome to Hangman!\n")

beginning()

def change():

    for character in secretWord:
        guess_word.append("-")

    print("The word You need to guess has", length_word, "characters")

    print("You can enter only 1 letter from a-z\n\n")

    print(guess_word)



def guessing():
    guess_taken = 1

    while guess_taken < 10:


        guess = input("Pick a letter\n").lower()

        if not guess in alphabet:
            print("Enter a letter from a-z alphabet")
        elif guess in letter_storage:
            print("You have already guessed that letter!")
        else: 

            letter_storage.append(guess)
            if guess in secretWord:
                print("You guessed correctly!")
                for x in range(0, length_word):
                    if secretWord[x] == guess:
                        guess_word[x] = guess
                        print(guess_word)

                if not '-' in guess_word:
                    print("Congrats! You won!")
                    break
            else:
                print("The letter is not in the word. Try Again!")
                guess_taken += 1
                if guess_taken == 10:
                    print(" Sorry, You lost! The secret word was",  secretWord)


change()
guessing()

print("Game Over!")