import random

number_of_streaks = 0
flips = 100

for experiment_Number in range(10000):
    coin_flips = []
    for i in range(flips):
        if random.randint(0, 1) == 0:
            coin_flips.append(0)
        else:
            coin_flips.append(1)


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
