import math
# Number of points
n = int(input())
# Initialise dictionary with points as keys and their coordinates as values
points = {}
# Add the points to the dictionary
for i in range(n):
    points[i] = [int(j) for j in input().split()]

# Store the coordinates of the first point
first_coor = points[0]
# The first time, the previous node is the first one
prev = first_coor
# Initialise the total distance variable
dist_total = 0

# Loop until no points are left
while True:
    # The minimum distance is initialised for each initial point
    mins = 10**5

    # Loop through the remaining points
    for key in points:
        # Calculate the distance between the previous point and the current one
        dist = math.sqrt((prev[0]-points[key][0])**2+(prev[1]-points[key][1])**2)

        # If the distance is less than the minimum
        if dist < mins:
            # Update the minimum distance
            mins = dist
            # And store the closest node
            key_min = key
    
    # Add the minimum distance between the previous point and one of the remaining ones
    dist_total += mins

    # Update the coordinates of the now previous point
    prev = points[key_min]
    # Remove the new node from the dictionary
    del points[key_min]

    # If all nodes have been considered
    if len(points) == 0:
        # Calculate the distance between the last node used and the first one
        dist_total += math.sqrt((prev[0]-first_coor[0])**2+(prev[1]-first_coor[1])**2)
        # Print the rounded result and exit the code
        print(round(dist_total))
        exit()
