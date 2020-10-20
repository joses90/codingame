import sys
import math

val = []
# Number of stock values during the timeline
n = int(input())

for i in input().split():
    # Value of the stock at each time
    v = int(i)
    val.append(v)

# Initialise the solution to 0, if no losses are registered, the loss will be 0
sol = 0

for i in range(n):
    # Iitialise the maximum value of the stock to the value at the first time
    if i == 0:
        max_num = val[i]
    # If the value at time i is bigger than the current maximum of the previous
    # times, update it
    elif val[i] > max_num:
        max_num = val[i]
    # If it is not, calculate the loss between the current maximum and the
    # value at time i
    else:
        diff = val[i] - max_num
        # If this loss the maximal loss at the moment, update the solution
        if diff < sol:
            sol = diff

print(sol)
