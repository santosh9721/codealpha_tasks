 import random

word_list = ['python', 'hangman', 'challenge', 'programming', 'developer']

secret_word = random.choice(word_list)
guessed_letters = []
attempts_remaining = 6

print("🎮 Welcome to Hangman!")
print("_ " * len(secret_word))

while attempts_remaining > 0:
    guess = input("\nGuess a letter: ").lower()


    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter a single alphabetic character.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct!")
    else:
        attempts_remaining -= 1
        print(f"❌ Incorrect! Attempts remaining: {attempts_remaining}")

    display_word = [letter if letter in guessed_letters else '_' for letter in secret_word]
    print("Word: " + ' '.join(display_word))

    if '_' not in display_word:
        print("\n🎉 Congratulations! You guessed the word:", secret_word)
        break
else:
    print("\n💀 Game over! The word was:", secret_word)
