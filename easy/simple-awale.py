# Distribution of grains for my opponent's and my bowls
op_bowls = [int(i) for i in input().split()]
my_bowls = [int(i) for i in input().split()]
# The bowl I am picking grains from
num = int(input())

# The amount of grains I will move
grains_to_move = my_bowls[num]
# Counter of grains moved
j = 0
# Empty the chosen bowl
my_bowls[num] = 0
# Did the distribution end at my reserve?
replay = 0

# Loop through the grains to be moved
while j < grains_to_move:
    # Bowl to put the current grain
    t = num + 1 + j

    # If it is less than 7
    if t < 7:
        # Put it in my bowl t
        my_bowls[t] += 1
        # If it is the last grain in the last of my bowls
        if t == 6 and j == grains_to_move - 1:
            # A replay will be needed
            replay = 1
    # If it is between 7 and 13
    # (not 14, because the opponent's reserve is not used for putting grains)
    elif t < 13:
        # Decrease the bowl number to match the next opponent bowl
        t -= 7
        # Put it in the opponent's bowl t
        op_bowls[t] += 1
    # Otherwise, a full cycle has been done
    else:
        # Decrease the bowl number to match my next bowl
        t -= 13
        # Put it in my bowl t
        my_bowls[t] += 1

    # Go to the next grain
    j += 1

# Print the solution
print(*op_bowls[:-1], end=" ");print(f"[{op_bowls[-1]}]")
print(*my_bowls[:-1], end=" ");print(f"[{my_bowls[-1]}]")

# If a replay is needed, print REPLAY
if replay == 1:
    print("REPLAY")
