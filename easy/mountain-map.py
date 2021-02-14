# Number of mountains
n = int(input())
# Heights for the mountains
height = [int(i) for i in input().split()]
# Maximum height
maxs = max(height)

# Look through each line to be printed
for i in range(maxs):
    # Initialise the line
    stri = ""

    # For each mountain
    for j in height:
        # Obtain the difference between the maximum height and the line possition
        diff = maxs - i

        # If the difference is greater than the height of the current mountain
        if diff > j:
            # Update the line with the necessary spaces
            stri += 2*j*" "
        # Otherwise, update the line
        else:
            stri += (diff - 1)*" " + "/" + (2*j-2-2*(diff - 1))*" " + "\\" + (diff - 1)*" "
    
    # Remove trailing spaces, print the line and go to the next line
    print(stri.rstrip())
