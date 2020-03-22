# HL component 3 - compares user guess with secret number

# To Do
# Set up number of guesses
# Count # of guesses
# if user runs out of guesses, print 'you lose'
# if user guesses the secret number within the number of guesses print 'well done'

secret = 7

guesses_allowed = 4

# initialise variables

guesses_left = guesses_allowed

num_won = 0

guess = ""

# start game

while guess != secret and guesses_left >= 1:

    guess = int(input("Guess: "))   # replace this function call in due course

    # if user has guesses left...
    if guesses_left >= 1:
        if guess > secret:
            print("Too high, try a lower number")
            print("You have {} guesses left".format(guesses_left - 1))
            guesses_left -= 1

        elif guess < secret:
            print("Too low, try a higher number")
            print("You have {} guesses left".format(guesses_left - 1))
            guesses_left -= 1

    elif guesses_left == 1:
        if guess > secret:
            print("Too high")

        if guess < secret:
            print("Too low")

if guess == secret:
    # If user guesses the secret number on the first try
    if guesses_left == guesses_allowed:
        print("You guessed the secret number on the first try")

    # If user guesses secret number correctly
    else:
        print("Congratulations, you guessed the secret number")

else:
    print("You have no more guesses left\n"
          "The correct number was {}".format(secret))


