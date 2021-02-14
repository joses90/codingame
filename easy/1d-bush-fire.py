# Number of tests
n = int(input())

# Look through the tests
for i in range(n):
    # Store the line
    line = input()
    # Initialise the position and the count of water drops
    j = 0
    count = 0

    # Look through the line
    while j < len(line):
        # If there is a fire in position j
        if line[j] == "f":
            # Put a water drop in j+1
            count += 1
            # And jump to j+3
            j += 3
        # If there is a dot, go to the next position
        else:
            j += 1

    # Print the solution for this line
    print(count)
