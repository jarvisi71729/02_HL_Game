# HL component 8 - Set up score mechanics

# To do
# Set up round and win counter
# update feedback statements


secret = 7
guesses_allowed = 4
rounds = 3

num_won = 0
rounds_played = 0

while rounds_played < rounds:
    guess = ""
    guesses_left = guesses_allowed

    while guess != secret and guesses_left >= 1:

        guess = int(input("Guess: "))
        guesses_left -= 1

        if guesses_left >= 1:

            if guess < secret:
                print("Too low, try a higher number. Guesses left: {}".format(guesses_left))

            elif guess > secret:
                print("Too high, try a lower number. Guesses left: {}".format(guesses_left))

        else:
            if guess < secret:
                print("Too low!")

            if guess > secret:
                print("Too high!")

    if guess == secret:
        if guesses_left == guesses_allowed - 1:
            print("Amazing! You guessed the secret number on the first try")

        else:
            print("Well done, you got it in {} guesses".format(guesses_allowed - guesses_left))
        num_won += 1

    else:
        print("Sorry - you lose this round as you have run out of guesses")

    print("Won: {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))
    rounds_played += 1
    print("Rounds left: {}".format(rounds - rounds_played))
