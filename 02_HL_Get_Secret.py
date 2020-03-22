# HL component 2 - Generates random number between low and high


import random

low = 1
high = 10


for item in range(1, 20):
    secret = random.randint(low, high)
    print(secret, end="\t")
