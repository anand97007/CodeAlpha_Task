import random

# Hangman stages
HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =========""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ========="""
]

# Word list
words = ['apple', 'chair', 'plant', 'house', 'train']
secret_word = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6
display_word = ['_' for _ in secret_word]

# Welcome message
print("🎮 Welcome to Hangman!")
print("Guess the word one letter at a time. You have 6 wrong guesses.\n")

# Game loop
while incorrect_guesses < max_incorrect and '_' in display_word:
    print(HANGMAN_PICS[incorrect_guesses])
    print("Word: ", ' '.join(display_word))
    print(f"Wrong guesses left: {max_incorrect - incorrect_guesses}")
    print("Guessed letters:", ' '.join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❗ Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Good guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        print("❌ Wrong guess!\n")
        incorrect_guesses += 1  # THIS LINE REDUCES GUESSES ON WRONG GUESS

# End of game
print(HANGMAN_PICS[incorrect_guesses])
if '_' not in display_word:
    print("🎉 You guessed the word:", secret_word)
else:
    print("💀 Game over! The word was:", secret_word)
