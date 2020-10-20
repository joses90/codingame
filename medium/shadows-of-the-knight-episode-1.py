import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]
n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
print("n = ", n, file=sys.stderr, flush=True)

xbat = x0
ybat = y0
min_pos = [0,0]
max_pos = [w,h]

# game loop
while True:
    # the direction of the bombs from batman's current location
    # (U, UR, R, DR, D, DL, L or UL)
    bomb_dir = input()

    # Update the top and bottom of the "square form"
    # according to the direction
    if bomb_dir[0] == "U":
        max_pos[1] = ybat
    elif bomb_dir[0] == "D":
        min_pos[1] = ybat
    elif bomb_dir[0] in ("L", "R"):
        min_pos[1] = ybat
        max_pos[1] = ybat

    # Update the left and right of the "square form"
    # according to the direction
    if bomb_dir[-1] == "L":
        max_pos[0] = xbat
    elif bomb_dir[-1] == "R":
        min_pos[0] = xbat
    elif bomb_dir[-1] in ("U", "D"):
        min_pos[0] = xbat
        max_pos[0] = xbat

    # Bisection method applied to the "square form" remaining
    xdir = math.floor((min_pos[0] + max_pos[0])/2)
    ydir = math.floor((min_pos[1] + max_pos[1])/2)

    # Store the needed result for each step
    sol = str(xdir) + " " + str(ydir)

    # Update Batman's position
    xbat = xdir
    ybat = ydir

    # the location of the next window Batman should jump to.
    print(sol)
