# Obtain the next group of cells to check for possible movements
# The count is an input to help visualise it (no need in fact to use it)
def fillnext(lis_cells,mat,count):

    # Initialise the set with the cells adjacent to the last group of cells
    se = set()

    # Look through each cell in the list
    for cell in lis_cells:
        # Obtain the adjacent cells to the cell
        lis = [(cell[0]-1,cell[1]),(cell[0],cell[1]-1),(cell[0],cell[1]+1),(cell[0]+1,cell[1])]
        # Add them to the set
        se |= set(lis)

    # Initialise the list of next cells
    lis = []

    # Look through the set of next cells    
    for c in se:
        # If the next cell is on the grid
        if c[0] in range(10) and c[1] in range(10):
            # And it has a "."
            if mat[c[1]][c[0]] == ".":
                # Replace that cell with the distance from the origin
                mat[c[1]][c[0]] = str(count)
                # Add this cell to the list of next cells
                lis.append(c)

    # Return the new list of next cells and the updated map
    return lis,mat

# Initialise the map
mat = []

# Look through each row
for i in range(10):
    # Store its value and add it to the map
    row = input()
    mat.append(list(row))

    # If the "C" is found, obtain its position
    if row.count("C") == 1:
        c_x = row.index("C")
        c_y = i

    # Same with the "M"
    if row.count("M") == 1:
        m_x = row.index("M")
        m_y = i


# Initialise the search with the child's cell
lis_cells = [(c_x,c_y)]
# Initialise the distance covered
count = 1

# Loop until the "M" is found
while True:
    # Flood fill the adjacent possible cells and provide the list of next cells
    lis_cells, mat = fillnext(lis_cells,mat,count)
    # Update the distance covered
    count += 1

    # Look through the list of next cells
    for cell in lis_cells:
        # If the cell is adjacent to the "M"
        if (cell[0] == m_x and abs(cell[1] - m_y) == 1) or (cell[1] == m_y and abs(cell[0] - m_x) == 1):
            # Print the solution and exit the code
            print(f"{count}0km")
            exit()
