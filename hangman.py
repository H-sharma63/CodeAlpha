import random

word_list = ["apple", "house", "train", "snake", "water"]
secret_word = random.choice(word_list)
guessed_word = ["_"] * len(secret_word)
guessed_letters = []
attempts_left = 6

print("🎯 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

while attempts_left > 0 and "_" in guessed_word:
    print("Word: " + " ".join(guessed_word))
    print("Guessed letters:", ", ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("⚠️ Please enter a single letter.\n")
        continue

    if guess in guessed_letters:
        print("🔁 You've already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
        print("✅ Correct!\n")
    else:
        attempts_left -= 1
        print(f"❌ Wrong guess. You have {attempts_left} attempts left.\n")

if "_" not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game over! The word was:", secret_word)
