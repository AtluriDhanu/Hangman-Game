import random

words = ["kawasaki", "yamaha", "ducati", "triumph", "suzuki"]
word = random.choice(words)
guessed_letters = []
attempts = 6
print("Welcome to Hangman Game - Bikes")

while attempts > 0:
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("\n Word: ", display_word)

    if"_" not in display_word:
        print("Congratulations! You guessed the word: ", word)
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed the word: ", word)
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct Guess!")
    else:
        attempts -= 1
        print("Wrong Guess!")
        print("Remaining Attempts: ", attempts)

if attempts == 0:
    print("\n Game Over!")
    print("The correct word was: ", word)
