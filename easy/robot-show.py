# THE TRICK FOR THIS ONE IS NOTICING THAT WHEN TWO BOTS COLLIDE,
# EACH ONE FOLLOWS THE TRAJECTORY THAT THE OTHER HAD BEFORE THE COLLISION
# AND THUS, THE LONGEST DISTANCE FROM A BOT TO AN EXIT IS EQUAL
# TO THE LONGEST TIME

# Length of the duct
l = int(input())
# Number of bots
n = int(input())
# Initialise minimum and maximum position for the bots
mins = l
maxs = 0

# Loop through every bot
for i in input().split():
    # If its position is more to the right than maxs
    if int(i) > maxs:
        # Update s
        maxs = int(i)

    # If its position is more to the left than mins
    if int(i) < mins:
        # Update mins
        mins = int(i)

# Calculate the distance between the leftmost bot and the right exit
max_left = l - mins
# Calculate the maximum distance (leftmost or right most bot?)
sol = max(maxs,max_left)
# Print the solution
print(sol)
