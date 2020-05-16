import random
#Flips a coin, 0/1 heads/tails
def flip():
    return random.randint(0,1)
#generate a list of coin flips
def list_of_flips(num):
    return [random.randint(0,1) for n in range(num)]
#generate this list as a consecutive string
def flips_str(num):
    return "".join(str(random.randint(0,1)) for n in range(num))
#print(flips_str(10))

#check for a streak inside our flips of "coin flips"
def chance_of_streak(streak_len, num_flips):
    flips = flips_str(num_flips)
    if ('0' * streak_len) in flips or ('1' * streak_len) in flips:
        return True
    else:
        return False
#Solve the problem, run our above 'checker' function through a loop for the num of runs (in this case 10000) and display the chance of having a streak of 6 '1's or 6 '0's in a list of 100 coin flips.

def coin_flip_streaks(runs, streak_len, num_flips):
    counter = 0
    for _ in range(runs):
        if chance_of_streak(streak_len, num_flips):
            counter += 1
    print(f"Chance of streaks: {(counter/runs) * 100}")

coin_flip_streaks(10000, 6, 100)