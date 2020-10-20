import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
dict = {}
lis = []
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    dict[ext] = mt
for i in range(q):
    fname = input()  # One file name per line.
    exten = fname
    dot = 0
    if '.' in fname:
        exten = fname.split('.')
        exten = exten[-1]
        dot = 1
        low = str.upper(exten)
        upp = str.lower(exten)
    if dot == 1 and low in dict:
            lis.append(dict[low])
    elif dot == 1 and upp in dict:
            lis.append(dict[upp])
    else:
        lis.append("UNKNOWN")

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


# For each of the Q filenames, display on a line the corresponding MIME type. If there is no corresponding type, then display UNKNOWN.
for l in lis:
    print(l)
