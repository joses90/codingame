import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
lis = []
for i in range(n):
    pi = int(input())
    lis.append(pi)

lis.sort()
max_diff = 10000000
for i in range(n-1):
    if lis[i+1] - lis[i] < max_diff:
        max_diff = lis[i+1] - lis[i]
# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(max_diff)
