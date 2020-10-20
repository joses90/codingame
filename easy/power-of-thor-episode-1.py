import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    x_diff = light_x - initial_tx
    y_diff = light_y - initial_ty
    if x_diff == 0:
        if y_diff < 0:
            go = "N"
            initial_ty = initial_ty - 1
        elif y_diff > 0:
            go = "S"
            initial_ty = initial_ty + 1
    elif y_diff == 0:
        if x_diff < 0:
            go = "W"
            initial_tx = initial_tx - 1
        elif x_diff > 0:
            go = "E"
            initial_tx = initial_tx + 1
    elif x_diff < 0:
        if y_diff < 0:
            go = "NW"
            initial_tx = initial_tx - 1
            initial_ty = initial_ty - 1
        elif y_diff > 0:
            go = "SW"
            initial_tx = initial_tx - 1
            initial_ty = initial_ty + 1
    elif x_diff > 0:
        if y_diff < 0:
            go = "NE"
            initial_tx = initial_tx + 1
            initial_ty = initial_ty - 1
        elif y_diff > 0:
            go = "SE"
            initial_tx = initial_tx + 1
            initial_ty = initial_ty + 1
    else:
        go = ""
    # A single line providing the move to be made: N NE E SE S SW W or NW
    print(go)
