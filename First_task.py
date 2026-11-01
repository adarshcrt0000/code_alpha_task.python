import random
words = ["python", "program", "computer", "keyboard", "developer"]

word = random.choice(words)
guessed = ["_"] * len(word)
guessed_letters = []
wrong_guesses = 0
max_wrong = 6

print("=== HANGMAN ===")
print("Guess the word one letter at a time. You have 6 wrong guesses.\n")

while wrong_guesses < max_wrong and "_" in guessed:
    print("Word:", " ".join(guessed))
    print("Wrong guesses left:", max_wrong - wrong_guesses)
    print("Guessed letters:", ", ".join(guessed_letters))

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Correct!\n")
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        wrong_guesses += 1
        print("Wrong!\n")

if "_" not in guessed:
    print("You won! The word was:", word)
else:
    print("Game over! The word was:", word)