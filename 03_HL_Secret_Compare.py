# HL component 3 - compares user guess with secret number

import random
# styles

underline_red = u"\u001b[31;4m"
red = u"\u001b[31m"

# ===

high_error = u"\u001b[31m\nToo {}high{}, try a lower number:\u001b[0m".format(underline_red, red)

low_error = u"\u001b[31m\nToo {}low{}, try a higher number:\u001b[0m".format(underline_red, red)

correct = u"\u001b[32m\nCongratulations! You guessed the secret number.\u001b[0m"


# ===

secret = random.randrange(0, 101)
print(secret)
guess = ""

while guess != secret:

    guess = int(input(u"\u001b[35;4m\nGuess:\u001b[m "))

    if guess > secret:

        print(high_error)

    elif guess < secret:

        print(low_error)

    else:
        print(correct)
