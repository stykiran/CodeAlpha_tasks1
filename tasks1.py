import random

# Predefined list of 5 words
words = ["apple", "zebra", "chair", "plant", "brush"]
word_to_guess = random.choice(words)

# Create a list of underscores the same length as the word
guessed_word = ["_"] * len(word_to_guess)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

print("Welcome to Hangman!")
print("Guess the word:", " ".join(guessed_word))

# Game loop
while incorrect_guesses < max_incorrect and "_" in guessed_word:
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        for i, letter in enumerate(word_to_guess):
            if letter == guess:
                guessed_word[i] = guess
        print("Correct!")
    else:
        incorrect_guesses += 1
        print("Wrong guess. Attempts left:", max_incorrect - incorrect_guesses)

    print("Current word:", " ".join(guessed_word))
    print("Guessed letters:", ", ".join(guessed_letters))

# Game result
if "_" not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", word_to_guess)
else:
    print("😢 Sorry, you've run out of guesses. The word was:", word_to_guess)
