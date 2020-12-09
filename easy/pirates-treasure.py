# Width and height of map
w = int(input())
h = int(input())
# Initialise values in map
maps = []

# Look through every row
for i in range(h):
    # Input the row
    row = input().split()
    # Transform the column values to integers
    row = [int(j) for j in row]
    # Add values to list
    maps.append(row)
    
# Look through every row
for i in range(h):
    # Look through every column
    for j in range(w):
        # If the cell is free, there could be a treasure
        if maps[i][j] == 0:
            # Initialise the count of adjacent obstacles            
            count = 0
            # Possible adjacent cells to cell i,j
            adjacent = [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]

            # Look through every possible adjacent cell
            for cell in adjacent:
                # If the possible cell is in the grid and its value is 1
                if cell[0] in range(h) and cell[1] in range(w) and maps[cell[0]][cell[1]] == 1:
                    # Increase the count of adjacent obstacles by 1
                    count += 1

            # If the count is a certain number, depending on if it is a corner, edge or inside
            if count == 8 or (count == 5 and (i in [0,h-1] or j in [0,w-1])) or (i in [0,h-1] and j in [0,w-1] and count == 3):
                # Print the result, the treasure has been found and exit the code
                print(f"{j} {i}")
                exit()
