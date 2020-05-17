# HL Component 11 - Maximum Guesses Calculator

import math

for item in range(0, 4):    # Loop component for easy testing...

    low = int(input("Low: "))    # use int check in due course
    high = int(input("High: "))

    range = high - low + 1
    max_raw = math.log2(range)  # finds maximum # of guesses using binary search
    max_upped = math.ceil(max_raw)  # rounds up (ceil --> ceiling)
    max_guesses = max_upped + 1
    print("Max Guesses: {}".format(max_guesses))

    print()
