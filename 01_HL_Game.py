# HL - Get (and check) user input

# To do
# Check that lowest is an integer
# Check that highest is more than lowest (lower bound only)
# Check that rounds is more than 1 (upper bound only
# Check that guess is between lowest and highest (lower & upper bound


# Number checking function

def intcheck(question, low=None, high=None):

    # sets up error messages

    if low is not None and high is not None:
            error = "Please enter an integer between {} and {} " \
                    "(inclusive)".format(low, high)

    elif low is not None and high is None:
        error = "Please enter an integer that is more than or " \
                "equal to {}".format(low)

    elif low is None and high is not None:
        error = "Please enter an integer that is less than or " \
                "equal to {}".format(high)

    else:
        error = "Please enter an integer"

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

    # Main routine

lowest = intcheck("Low Number: ")
highest = intcheck("High Number: ", lowest + 1)
rounds = intcheck("Rounds: ", 1)
guess = intcheck("Guess: ", lowest, highest)
