# If a change has been done, print the solution and exit the whole code
def change_done(mat):
    for line in mat:
        print("".join(line))
    exit()

# Initialise the board
mat = []

# Look through the rows
for i in range(3):
    # Add the row to the board
    line = list(input())
    mat.append(line)

# Look through every row
for j,line in enumerate(mat):
    # If there are two Os and one dot in this row
    if line.count("O") == 2 and line.count(".") == 1:
        # Update the empty square and print the result
        mat[j][line.index(".")] = "O"
        change_done(mat)

# Look through every column
for j,line in enumerate(list(map(list,zip(*mat)))):
    # If there are two Os and one dot in this column
    if line.count("O") == 2 and line.count(".") == 1:
        # Update the empty square and print the result
        mat[line.index(".")][j] = "O"
        change_done(mat)

# Look through the possible diagonal solutions
# If any of them is available, update the empty square and print the result
if mat[0][0] == "O" and mat[1][1] == "O" and mat[2][2] == ".":
    mat[2][2] = "O"
    change_done(mat)
elif mat[0][0] == "O" and mat[1][1] == "." and mat[2][2] == "O":
    mat[1][1] = "O"
    change_done(mat)
elif mat[0][0] == "." and mat[1][1] == "O" and mat[2][2] == "O":
    mat[0][0] = "O"
    change_done(mat)
elif mat[2][0] == "O" and mat[1][1] == "O" and mat[0][2] == ".":
    mat[0][2] = "O"
    change_done(mat)
elif mat[2][0] == "O" and mat[1][1] == "." and mat[0][2] == "O":
    mat[1][1] = "O"
    change_done(mat)
elif mat[2][0] == "." and mat[1][1] == "O" and mat[0][2] == "O":
    mat[2][0] = "O"
    change_done(mat)

# If the code has not been exited, there is no winning move
print("false")
