# Number of different descriptions of the road
n = int(input())
# Position of the car at the beginning and commands separated by ";"
commands = input().split(";")
# Extract the initial position of the car
x = int(commands.pop(0))
# Initialise the list of direction for each line
direc = []

# Look through each command
for val in commands:
    # For each command type: "S","R" or "L"
    for j in range(int(val[:-1])):
        # Add the direction the amount of times the integer mentions
        direc.append(val[-1])

# Initialise the list of road lines
road = []
# Initialise the length of the road (amount of lines)
length_road = 0

# For each type of road
for i in range(n):
    # Store the repetition number and the road design
    [r,roadpattern] = input().split(";")
    # Update the length of the road
    length_road += int(r)
    # Add r times the design of the road to the road list
    for j in range(int(r)):
        road.append(roadpattern)

# Convert the initial position to starting from 0 index
x -= 1
# Initialise counter for road line
k = 0

# Loop through every road line
while k < length_road:

    # If the direction is right, increase the car position by 1
    if direc[k] == "R":
        x += 1
    # If the direction is left, decrease the car position by 1
    elif direc[k] == "L":
        x -= 1

    # Replace index x in the k line by the car "#"
    line = road[k][:x] + "#" + road[k][x+1:]

    # Print the current line
    print(line)

    # Update the road line
    k += 1
