# Height and width for each grid
# The width will not be used
height, width = [int(i) for i in input().split()]
# Initialise the list of values for each grid
grid_num = []
grid_xo = []

# Add the values of each grid to their list
for i in range(height):
    grid_num.extend(input().split())
for i in range(height):
    grid_xo.extend(input().split())

# Create a list with the values corresponding to the "X" sign
num = [grid_num[j] for j in range(len(grid_xo)) if grid_xo[j] == "X"]

# For each value
for j,val in enumerate(num):
    # If the value is positive, replace it for a 1
    if int(val) > 0:
        num[j] = 1
    # Otherwise, for a -1
    else:
        num[j] = -1

# Initialise a counter
k = 1

# Look through the list of 1s and -1s
while k < len(num):
    # If a number is equal to the previous one, the solution is false
    # and the code can be exited
    if num[k-1] == num[k]:
        print("false")
        exit()
    k += 1

# If the code has not been exited, the solution is true
print("true")
