import random

# Word list
words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

# Choose a random word
original_word = random.choice(words)

# Scramble the word manually
scrambled = list(original_word)
shuffled_word = ''.join(scrambled)

# Keep scrambling until it's different from the original
while shuffled_word == original_word:
    i = 0
    while i < len(scrambled):
        j = random.randint(0, len(scrambled) - 1)
        temp = scrambled[i]
        scrambled[i] = scrambled[j]
        scrambled[j] = temp
        i = i + 1
    shuffled_word = ''.join(scrambled)

print("You are invited to Word Scramble Game!")
print("Unscramble this word:", shuffled_word)

# Player has 3 attempts
attempts = 3
while attempts > 0:
    guess = input("Enter your guess: ").lower()
    if guess == original_word:
        print("Bravo! You win!!!!")
        attempts = 0  # Exit loop
    else:
        attempts = attempts - 1
        if attempts > 0:
            print("Wrong guess. Try again! Attempts left:", attempts)
        if attempts == 0 and guess != original_word:
            print("Out of attempts! The correct word was:", original_word)