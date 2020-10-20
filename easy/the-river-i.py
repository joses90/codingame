import sys
import math

r_1 = int(input())
r_2 = int(input())

r_min = min(r_1, r_2)
r_max = max(r_1, r_2)

def sum_digits(num):
    # Function to obtain the sum of the digits of a number
    res = 0
    lis = list(str(num))
    for i in lis:
        res = res + int(i)
    return res

# Loop if the last number of both series are not the same
while r_max != r_min:
    # Sum digits for the smallest number from the last of both series
    add = sum_digits(r_min)
    # Update the last number of that serie
    r_min = r_min + add
    # If the new last number is bigger than the last number of the other series,
    # change which one is the small/big one
    if r_min > r_max:
        [r_max, r_min] = [r_min, r_max]

print(r_max)
