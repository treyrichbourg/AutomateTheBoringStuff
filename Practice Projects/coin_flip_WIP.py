import random
num_of_streaks = 0
#make a list of random "Heads" and "Tails"
def flip(num):
    return [random.randint(0,1) for n in range(num)]
#make a list of random "Heads" and "Tails" as strings, ['1', '0', '0', '1']
# def flip_str(num):
#     return [str(random.randint(0,1)) for n in range(num)]
#make a continuous string of our generated list    
def flip_str(num):
    return "".join(str(random.randint(0,1)) for n in range(num))
#check list for a streak
# def streak_in_flips(current_streak, n_flips):
#     return current_streak in flip_str(n_flips)
#check list of 100 flips for '000000' or '111111' num_flips times and return True or False
def streak_in_flips(streak, num_flips):
    flips = flip_str(num_flips)
    if ('0' * streak) in flips or ('1' * streak) in flips:
        return True
    else:
        return False
#Finish him
def chance_streak(iterations, streak, num_flips):
    count = 0
    for iteration in range(iterations):
        if streak_in_flips(6, 100):
            count += 1
    print('Chance of streak: %s%%' %(count/100))

chance_streak(10000, 6, 100)

