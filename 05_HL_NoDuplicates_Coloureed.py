# HL Component 5 - no duplicate guesses

# To Do
# Set up empty list called already_guessed
# when user guesses, add guess to list
# for each guess, check that number is not in already_guessed

# HL Component 5 - prevent duplicate guesses


def intcheck(question, low=None, high=None):

    # sets up error messages

    if low is not None and high is not None:
            error = u"\u001b[31mPlease enter an integer between {} and {} " \
                    "(inclusive)".format(low, high)

    elif low is not None and high is None:
        error = u"\u001b[31mPlease enter an integer that is more than or " \
                "equal to {}".format(low)

    elif low is None and high is not None:
        error = u"\u001b[31mPlease enter an integer that is less than or " \
                "equal to {}".format(high)

    else:
        error = u"\u001b[31mPlease enter an integer"

    while True:

        try:
            response = int(input(question))

            # Checks response is not too low

            if low is not None and response < low:
                print(error)
                continue

            # Checks response is not too high

            if high is not None and response > high:
                print(error)
                continue

            return response

        except ValueError:
            print(error)
            continue


secret = 7
guesses_allowed = 5

already_guessed = []
guesses_left = guesses_allowed
num_won = 0

guess = ""

while guess != secret and guesses_left >= 1:

    guess = intcheck(u"\u001b[35mGuess: ")   # replace this function call in due course

    # checks that guess is not a duplicate
    if guess in already_guessed:
        print(u"\u001b[31mYou already guessed that number! Please try again. \u001b[m"
              u"\u001b[33mYou *still* have {} guesses left".format(guesses_left))
        continue

    guesses_left -= 1
    already_guessed.append(guess)

    if guesses_left >= 1:

        if guess < secret:
            print(u"\u001b[31mToo low, Try a higher number\u001b[m\n"
                  u"\u001b[33mYou have {} guesses left".format(guesses_left))

        elif guess > secret:
            print(u"\u001b[31mToo high, Try a lower number\u001b[m\n"
                  u"\u001b[33mYou have {} guesses left".format(guesses_left))

    else:
        if guess < secret:
            print(u"\u001b[31mToo low!")

        if guess > secret:
            print(u"\u001b[31mToo high")

if guess == secret:
    if guesses_left == guesses_allowed - 1:
        print(u"\u001b[32mAmazing! You guessed the secret number on the first try")

    else:
        print(u"\u001b[32mWell done, you got guessed the secret number in {} tries".format(len(already_guessed)))
    num_won += 1

# if user loses the game without guessing secret number

else:
    print(u"\u001b[34mSorry - you lose this round as you have run out of guesses")
