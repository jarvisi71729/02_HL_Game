# Hl component 9b - End Game Stats

# To Do
# Set up Game Play list with each round's results
# Set up average, best and worst scores (see 09a Stats_experiment)


secret = 7
guesses_allowed = 4
rounds = int(input("How many rounds would you like to play? "))
game_stats = []

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
                print("Too high, try a lower number. Guesses left: {}".format(guesses_left))

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

    game_stats.append(guesses_allowed - guesses_left)
    print("Won: {} \t | \t Lost: {}".format(num_won, rounds_played - num_won + 1))
    rounds_played += 1

# print each round's outcome...

print()
print("*** Game Scores ***")
list_count = 1
for item in game_stats:

    # indicates if game has been won or lost

    if item > guesses_allowed:
        status = "lost, ran out of guesses"

    else:
        status = "won"

    print("Round {}: {} ({})".format(list_count, item, status))
    list_count += 1

# Calculate (and then print) game statistics

game_stats.sort()
best = game_stats[0]
worst = game_stats[-1]
average = sum(game_stats)/len(game_stats)

print()
print("*** Summary Statistics ***\n")
print("Best: {}\n".format(best))
print("Worst: {}\n".format(worst))
print("Average: {:.2f}".format(average))
