# Import itertools to help with counting the ocurrences of each number
from itertools import chain

# Possible numbers in grid
numbers = "123456789"
# List to store the values in the grid
maps = []

# Store the values
for i in range(9):
    maps.append(input().split())

# Convert the 2d list into a 1d list
lis = list(chain(*maps))

# Count the ocurrences of each number in the full matrix
for i in numbers:
    # If any number is more than 9 times, the solution is "false"
     if lis.count(i) != 9:
        print("false")
        exit()

# For each row
for i in maps:
    # Initialise the sum variable
    sum = 0
    # For each column, add the value to sum
    for j in i:
        sum += int(j)
    # If the sum is not 45, the solution is "false"
    if sum != 45:
        print("false")
        exit()

# Transpose the matrix to do the same analysis for the columns
trans = list(map(list,zip(*maps)))

# For each column
for i in trans:
    # Initialise the sum variable
    sum = 0
    # For each row add the value to sum
    for j in i:
        sum += int(j)
    # If the sum is not 45, the solution is "false"
    if sum != 45:
        print("false")
        exit()

# Divide the matrix into 9 sub-grids: key:[x_start,x_end+1,y_start,y_end+1]
# x changes for each column and y for each row
grids = {0:[0,3,0,3],1:[3,6,0,3],2:[6,9,0,3],3:[0,3,3,6],4:[3,6,3,6],5:[6,9,3,6],6:[0,3,6,9],7:[3,6,6,9],8:[6,9,6,9]}
# Initialise the list containing the numbers in each grid
check_grids = [[] for i in range(10)]
# Initialise the variable to control if an error has been found
end = 0

# For every row
for i,line in enumerate(maps):
    # For every row
    for j,val in enumerate(line):
        # For each sub-grid limits
        for key in grids:
            # If the cell is inside the sub-grid
            if grids[key][0] <= j < grids[key][1] and grids[key][2] <= i < grids[key][3]:
                # Add that value to the key position of check_grids and go to the next cell
                check_grids[key].append(val)
                break

    # For each sub-grid
    for k in check_grids:
        # If all sub-grid values are in included
        if len(k) == 9:
            # And none are repeated, the solution is "false"
            if len(set(k)) != 9:
                print("false")
                exit()

print("true")
