# Number of horses
n = int(input())
# Initialise list of horses
horses = []

# Look through every horse and add its speed and elegance to the list
for i in range(n):
    horses.append([int(j) for j in input().split()])

# Initialise the minimum strength
mins = 100000000

# For every horse
for i in range(len(horses)):
    # Comparing it to the horses after him
    # The difference between horse a and b is the same as between b and a
    for j in range(i,len(horses)):
        # Do not compare a horse with itself
        if i == j:
            pass
        # If it is another horse
        else:
            # Obtain the strength
            diff = abs(horses[j][0] - horses[i][0]) + abs(horses[j][1] - horses[i][1])
            # If it is less than the minimum, update the minimum value
            if diff < mins:
                mins = diff

# Print the result
print(mins)
