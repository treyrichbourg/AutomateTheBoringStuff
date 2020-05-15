import random

number_of_streaks = 0
flips = 100



In [81]: for experiment_Number in range(10000): 
    ...:     coin_flips = [random.randint(0, 1) for n in range(100)] 
    ...:     for i in coin_flips: 
    ...:         if i == 0: 
    ...:             count_i += 1 
    ...:         else: 
    ...:             count_i = 0 
    ...:         if count_i == 6: 
    ...:             number_of_streaks += 1 
    ...:             count_i = 0 
    ...: print(number_of_streaks) 
    ...:  
    ...:  
    ...:              
    ...:                                                                                      
7929

In [82]:                                                                                      

In [82]:    


num_streaks = 0
def flip():
    return random.randint(0, 1)

def list_of_flips(num):
    return[flip() for n in range(num)]

def flips_str(num):
    return "".join([str(flip()) for n in range(num)])

for trial_number in range(20):
    if streak_in_flips(6, 100):
        print("Streak of 6 heads or tails present")
    else:
        print("Streak not found")