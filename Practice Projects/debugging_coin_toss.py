#! usr/bin/env python3
import random, logging

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s"
)
logging.disable()

guess = ""
while guess not in ("heads", "tails"):
    print("Guess the coin toss! Enter heads or tails:")
    guess = input()
    logging.debug("User inputting guess")
    if guess not in ("heads", "tails"):
        logging.debug(
            "If user doesn't input 'heads' or 'tails' then prompt them for the proper input and repeat loop"
        )
        print("Please input heads or tails")
        continue
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
if toss == 0 and guess == "tails" or toss == 1 and guess == "heads":
    logging.debug("Checking to see if the toss matches the guess")
    print("You got it!")
else:
    logging.debug("Second guess attempt if the user got the first one wrong")
    print("Nope! Guess again!")
    guess = input()
    if toss == 0 and guess == "tails" or toss == 1 and guess == "heads":
        logging.debug("Checking to see if the toss matches the guess")
        print("You got it!")
    else:
        logging.debug("User got both guesses wrong")
        print("Nope. You are really bad at this game.")
