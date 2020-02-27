# Higher / Lower version 2
# Author: Iszac Jarvis
# Date: 26/09/2019

# v1: Basic program works but it does not loop yet.
# v2: Program loops and uses a random number (instead of 48)
# v3: Shows number of guesses left,
# has special message if user guesses correctly on the first time
# v4: Checks numbers are valid <uses a function which is beyond L1...
# v5: Allows user to choose number of rounds (maximum 5)
# v6: Does not allow duplicate guesses anymore.
# v7: Removed 'secret number' answer. We are done!

# generates random integer
import random


# number checking functions

def num_check(question, low, high):

    error = "Please enter a number between {} and {}".format(low, high)

    valid = False
    while not valid:
        try:
            response = int(input(question))
            if low-1 < response < high+1:
                return response
            else:
                print(error)

        except ValueError:
            print("You did not enter an INTEGER. Please try again")


def int_check(question):
    valid = False
    while not valid:
        try:
            response = int(input(question))
            valid = True
            return response

        except ValueError:
            print("You did not enter an INTEGER. Please try again")

# constants / initial values

min_num = int_check("What would you like to be the smallest possible number to be for this game? ")

max_num = num_check("\nWhat would you like to be the highest possible number to be for this game? ", min_num + 1, 1000000)

max_guesses = num_check("\nWhat is the maximum amount of guesses you would like? ", 1, max_num)

num_rounds = num_check("\nHow many rounds would you like to play? (maximum 5): ", 1, 5)

best_guess = max_guesses

rounds_won = 0

round_counter = 0
while round_counter < num_rounds:

    # generates random integer based on user's specs

    secret = random.randrange(min_num, max_num)

    print("Secret: ", secret)

    round_counter += 1

    num_guess = 0

    already_guessed = []  # empty list for numbers that have already been guessed

    guess = -1

    print("========")

    if round_counter == 1:
        print("Round 1! Begin!")

    if round_counter > 1:
        print("Round {}!".format(round_counter))

    if round_counter == num_rounds:
        print("Final round!")

    print("========")

    while guess != secret and num_guess <= max_guesses:

        # get user guesses (and check that they are valid)

        # Had to use string concatenation to get question to display nicely

        # Had to create question separately to allow it to display min / max with

        question = "Guess a number between "+str(min_num)+" and "+str(max_num) + ": "

        guess = num_check(question, min_num, max_num)

        # loop checks that guess has not been tried before

        while guess in already_guessed:
            guess = num_check("You already guessed that number, please try again: ", min_num, max_num)

        num_guess += 1

        already_guessed.append(guess)

        # Compare guess with secret number

        # correct guess, user wins

        if max_guesses - num_guess == 0 and guess == secret:
            print("Congratulations, you guessed the secret number in ", num_guess, "tries\n")
            rounds_won += 1

        # user has run out of guesses
        elif max_guesses - num_guess == 0:
            print("You lose! You have guessed ", max_guesses, "times\n")
            break

        # too high
        elif guess > secret:
            print("Too high, try a lower number. You have", max_guesses - num_guess, "guesses left\n")

        # too low
        elif guess < secret:
            print("Too low, try a higher number. You have", max_guesses - num_guess, "guesses left\n")

        else:
            rounds_won += 1
            if guess == secret and num_guess == 1:
                print("Incredible! Your luck is off the charts! You guessed the secret number on the first try!!")

            else:
                print("\nCongratulations. You guessed the number in", num_guess, "tries")

    # update best score
    if num_guess < best_guess:
        best_guess = num_guess

# print end of game info

win_percentage = rounds_won/round_counter*100

print("Your best score was:", best_guess)

print()

print("You played ", round_counter, "rounds!")

print()

print("Out of your total amount of rounds played, you won ", rounds_won, "rounds")

print()

print("Overall, your win percentage across all rounds was {}%".format(win_percentage))
