import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse
close = math.inf
close_pos = math.inf
close_neg = -math.inf
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if t >= 0 and t < close_pos:
        close_pos = t
    elif t < 0 and t > close_neg:
        close_neg = t
    print(t, file=sys.stderr, flush=True)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

if n == 0:
    close = 0
elif close_pos <= abs(close_neg):
    close = close_pos
else:
    close = close_neg

print(close)
