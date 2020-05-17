# HL Game Completed

# test statement


def h1_statement(statement):
    # print()
    print(statement)
    print()


# number checking functions (between low & high)


def int_check(question, low, high):
    valid = False
    while not valid:

        try:
            response = int(input(question))
            if low <= response <= high:
                print()
                return response
            else:
                print(u"\u001b[31mEnter a number between {} and {}\u001b[0m\n".format(low, high))

        except ValueError:
            print(u"\u001b[31mPlease Enter An Integer.\u001b[0m\n")

# colours


blue = "\u001b[34m"
pink = "\u001b[35m"
light_blue = "\u001b[36m"
red = "\u001b[31m"
gold = "\u001b[33m"
green = "\u001b[32m"

# start of loop


keep_going = ""
while keep_going == "":

    import random

    # define low and high values
    low = 1
    high = 10

    # guess between low & high statement
    h1_statement(u"\u001b[34mGuess The Secret Number between {} and {}".format(low, high))

    # generates secret number
    SECRET = random.randint(low, high)
    random = random
    import math

    # guess calculator
    guesses = high - low + 1
    already_guessed = []
    max_raw = math.log2(guesses)
    max_upped = math.ceil(max_raw)
    max_guesses = max_upped + 1
    h1_statement("You have {} Guesses".format(max_guesses))
    round_number = 1
    game_stats = []

    guesses_allowed = max_guesses

    # amount of rounds
    rounds = int_check(u"\u001b[36mHow many rounds would you like to play? \u001b[0m", 1, 5)

    num_won = 0
    rounds_played = 0

    # valid loop (user has not lost)
    while rounds_played < rounds:
        guess = "1"
        guess_number = 1
        guesses_left = guesses_allowed

        # round counter
        while guess != SECRET and guesses_left >= 1:
            h1_statement(u"\u001b[34mRound: {}\u001b[0m".format(round_number))

            # Input guess
            guess = int_check(u"\u001b[35mGuess ({}): \u001b[0m".format(guess_number), 1, high)
            guess_number += 1
            guesses_left -= 1

            # already guessed check
            if guess in already_guessed:
                h1_statement(u"\u001b[31mYou already guessed this number, "
                             "you still have {} guesses\u001b[0m".format(guesses_left + 1))
                guesses_left += 1
                guess_number -= 1
                continue

            already_guessed.append(guess)

            # compare guess to secret num
            if guesses_left >= 1:
                if guess < SECRET:
                    h1_statement(u"\u001b[31mToo low.      {} Guesses left\u001b[0m".format(guesses_left))

                elif guess > SECRET:
                    h1_statement(u"\u001b[31mToo high.     {} Guesses left\u001b[0m".format(guesses_left))

        # if guess is secret (correct)
        if guess == SECRET:

            # first guess
            if guesses_left == guesses_allowed - 1:
                h1_statement("Good job! You guessed the number in one guess.   **Round Won**")
                num_won += 1
                round_number += 1
                SECRET = random.randint(low, high)
                already_guessed = []

            # guess < 1 (more than 1 guess)
            else:
                h1_statement(u"\u001b[32mWell done! You guessed the number in {} guesses.   **Round Won**\u001b[0m".format(
                    guesses_allowed - guesses_left))
                num_won += 1
                round_number += 1
                SECRET = random.randint(low, high)
                already_guessed = []

        # if user runs out of guesses
        else:
            h1_statement(u"\u001b[31mYou ran out of guesses. The secret was: {}  **Round Lost**\u001b[0m".format(SECRET))
            already_guessed = []

            guesses_left -= 1
            round_number += 1
            SECRET = random.randint(low, high)

        # end of round info : win/lost tracker
        game_stats.append(guesses_allowed - guesses_left)
        print(u"\u001b[32mWON: {}             \u001b[31mLOST: {}\u001b[0m\n".format(num_won, rounds_played - num_won + 1))
        rounds_played += 1

    # elaborated win/lost tracker (round specific)
    h1_statement(u"\u001b[34mGame Score\u001b[0m")
    list_count = 1
    for item in game_stats:

        if item > guesses_allowed:
            status = u"\u001b[31mLOST\u001b[0m"

        else:
            status = u"\u001b[32mWON\u001b[0m"

        print(u"\u001b[36mRound {}: Guesses: {}  ({}\u001b[36m)\u001b[0m".format(list_count, item, status))
        list_count += 1

    # game stats
    game_stats.sort()
    best = game_stats[0]
    worst = game_stats[-1]
    average = sum(game_stats) / len(game_stats)

    # game stats : best guess (round), worst guess (round), average guesses (game)
    while rounds_played < rounds:
        print(u"\u001b[34mRound:{}\u001b[0m".format(rounds_played + 1))
        rounds_played += 1

    print(u"\u001b[32m\nWell done! You have completed the game!\u001b[0m")
    print()
    print(u"\u001b[34m*** YOUR GAME STATISTICS ***\u001b[0m")
    print(u"\u001b[32m*BEST* guess in 1 round: {}\u001b[0m".format(best))
    print(u"\u001b[31m*WORST* guess in 1 round: {}\u001b[0m".format(worst))
    print(u"\u001b[35m*AVG* guesses per game: {:.2f}\u001b[0m".format(average))
    print()

    # allows user to play again
    keep_going = input(u"\u001b[34mPress <enter> to play again or any key to quit:\u001b[0m")
    print()
print(u"{}Thank {}you {}for {}playing {}the {}game :]".format(blue, pink, light_blue, green, gold, red))
