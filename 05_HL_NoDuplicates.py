# HL Component 5 - no duplicate guesses

# To Do
# Set up empty list called already_guessed
# when user guesses, add guess to list
# for each guess, check that number is not in already_guessed

# HL Component 5 - prevent duplicate guesses

secret = 7
guesses_allowed = 5

already_guessed = []
guesses_left = guesses_allowed
num_won = 0

guess = ""

while guess != secret and guesses_left >= 1:

    guess = int(input("Guess: "))   # replace this function call in due course

    # checks that guess is not a duplicate
    if guess in already_guessed:
        print("You already guessed that number! Please try again. "
              "You *still* have {} guesses left".format(guesses_left))
        continue

    guesses_left -= 1
    already_guessed.append(guess)

    if guesses_left >= 1:

        if guess < secret:
            print("Too low, Try a higher number\n"
                  "You have {} guesses left".format(guesses_left))

        elif guess > secret:
            print("Too high, Try a lower number\n"
                  "You have {} guesses left".format(guesses_left))

    else:
        if guess < secret:
            print("Too low!")

        if guess > secret:
            print("Too high")

if guess == secret:
    if guesses_left == guesses_allowed - 1:
        print("Amazing! You guessed the secret number on the first try")

    else:
        print("Well done, you got guessed the secret number in {} tries".format(len(already_guessed)))
    num_won += 1

else:
    print("Sorry - you lose this round as you have run out of guesses")
