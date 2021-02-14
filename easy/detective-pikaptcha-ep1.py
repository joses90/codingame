# Width and height of maze
width, height = [int(i) for i in input().split()]
# Initialise map
mat = []

# Store the columns of the map for each height
for i in range(height):
    mat.append(input())

# Look through each row
for row in range(height):
    # Initialise the row solution
    sol = ""

    # Look through each column
    for column in range(width):
        # If the value for this cell is "#"
        if mat[row][column] == "#":
            # Add it to the solution
            sol += "#"
        # Otherwise, if it is not a wall
        else:
            # Obtain the adjacent cells
            adjacent = [(row-1, column), (row+1, column), (row, column-1), (row, column+1)]
            # Initialise the number of neighbours this cell has
            neighb = 0

            # Look through the list of adjacent cells
            for cell in adjacent:
                # If the adjacent cell is in the grid and does not have a wall
                if cell[0] in range(height) and cell[1] in range(width) and mat[cell[0]][cell[1]] != "#":
                    # Increase the neighbours amount by 1
                    neighb += 1
            
            # Add the amount of neighbours to the row solution
            sol += str(neighb)
    # Print the row solution
    print(sol)
