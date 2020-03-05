# HL component 3 - compares user guess with secret number

# ===

high_error = u"\u001b[31mToo high, try a lower number:\u001b[0m"

low_error = u"\u001b[31mToo low, try a higher number:\u001b[0m"

correct = u"\u001b[32mCongratulations! You guessed the secret number.\u001b[0m"

# ---

secret = 7

guess = ""

while guess != secret:

    guess = int(input("Guess: "))

    if guess > secret:

        print(high_error)

    elif guess < secret:

        print(low_error)

    else:
        print(correct)
