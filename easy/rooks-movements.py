# Rook position
rook_position = input()
# Number of pieces on the board (other than my rook)
nb_pieces = int(input())
# Possible values of column
c = "abcdefgh"
# List to store the cells with ally pieces, opponent pieces and the possible solutions
ally = []
oppo = []
sol = []

# Look through the pieces placed
for i in range(nb_pieces):
    # Store if it is mine or the other player's and its position
    inputs = input().split()
    colour = int(inputs[0])
    one_piece = inputs[1]

    # If it is mine, add the position to the ally list
    if colour == 0:
        ally.append(one_piece)
    # If it is the opponent's, add the position to the opponent list
    else:
        oppo.append(one_piece)

# Check cells within the same row but for the previous columns
# Initialise the cells to be checked
new = rook_position
while True:
    # If the cell is in the board
    if new[0] != "a":
        # Store the previous cell
        new = c[c.index(new[0])-1] + new[1]

        # If there is an ally piece, stop this check (no more available cells)
        if new in ally:
            break
        # If there is an opponent piece, store the value for this cell
        # and stop this check (no more available cells)
        elif new in oppo:
            sol.append(f"R{rook_position}x{new}")
            break
        # Otherwise, store the value for this cell
        else:
            sol.append(f"R{rook_position}-{new}")
    # Otherwise, stop this check
    else:
        break

# Check cells within the same row but for the next columns
# Similar execution to the first while loop
new = rook_position
while True:
    if new[0] != "h":
        new = c[c.index(new[0])+1] + new[1]

        if new in ally:
            break
        elif new in oppo:
            sol.append(f"R{rook_position}x{new}")
            break
        else:
            sol.append(f"R{rook_position}-{new}")
    else:
        break

# Check cells within the same column but for the previous rows
# Similar execution to the first while loop
new = rook_position
while True:
    if new[1] != "1":
        new = new[0] + str(int(new[1])-1)

        if new in ally:
            break
        elif new in oppo:
            sol.append(f"R{rook_position}x{new}")
            break
        else:
            sol.append(f"R{rook_position}-{new}")
    else:
        break

# Check cells within the same column but for the next rows
# Similar execution to the first while loop
new = rook_position
while True:
    if new[1] != "8":
        new = new[0] + str(int(new[1])+1)
        
        if new in ally:
            break
        elif new in oppo:
            sol.append(f"R{rook_position}x{new}")
            break
        else:
            sol.append(f"R{rook_position}-{new}")
    else:
        break

# Sort the list of solutions and print them
for s in sorted(sol):
    print(s)
