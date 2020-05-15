def sum_of_low(n):
    n.sort()
    return n[0] + n[1]

test = [5, 2, 15, 12]
print(sum_of_low(test)) #should return 7
test[2] = 1
print(sum_of_low(test)) #should return 3