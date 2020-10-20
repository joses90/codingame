import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
bin01_notfull = ''.join(format(ord(x), 'b') for x in message)
bin01 = bin01_notfull.zfill(7)
l = len(bin01)

bin0 = ""
i = 0

while i < l:
    h = 1
    t = i
    try:
        while bin01[i] == bin01[i+1]:
            i = i + 1
            h = h + 1
            if i+1 == l:
                break
    except IndexError:
        h = 1
    if h == 1:
        i = i + 1
    if int(bin01[t]) == 0:
        bin0 = bin0 + "00 " + "0"*h + " "
    else:
        bin0 = bin0 + "0 " + "0"*h + " "
    i = t + h

sol = bin0.strip()
print(sol)
