# To help divide the strings
import re

# Number of lines
n = int(input())
# Initialise list with formula
mat = []

# Look through each line
for i in range(n):
    # Convert line into elements of length 3
    compound = re.findall("...",input())
    # Initialise list for this line
    lis = []

    # Look through each group
    for j in compound:
        # If it is a space, add 0 to the line list
        if j == "   ":
            lis.append(0)
        # If it is a bond, add its number to the line list
        elif j[0] == "(" and j[2] == ")":
            lis.append(int(j[1]))
        # Otherwise, if it is a unit of carbon, add its amount of hydrogens as a string
        else:
            lis.append(j[2])

    # Add the line list to the matrix list
    mat.append(lis)

# Look through every line in the matrix
for i in range(n):
    # Look through every row for that line
    for j in range(len((mat[i]))):
        # If it is in in an even row and column and it is not a 0 value i.e. a unit of carbon
        if i%2 == 0 and j%2 == 0 and mat[i][j] != 0:
            # Initialise the bonds with the amount of hydrogens
            carbon = int(mat[i][j])
            # Store the adjacent cells to i,j
            adjacent = [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]

            # Look through the list of adjacent cells
            for cell in adjacent:
                # If the cell is in the grid
                if cell[0] in range(n) and cell[1] in range(len(mat[cell[0]])):
                    # Add the bonds found to the carbon variable
                    carbon += mat[cell[0]][cell[1]]
            
            # If the sum of hydrogens plus adjacent bonds is not 4, the solution is INVALID
            # Exit the loop
            if carbon != 4:
                print("INVALID")
                exit()

# If no error has been found, the solution is VALID
print("VALID")
