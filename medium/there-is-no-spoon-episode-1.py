import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
print("width = ", width, file=sys.stderr, flush=True)
print("height = ", height, file=sys.stderr, flush=True)
# Create the matrix in a 2d array in variable mat
mat = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    line = list(line)
    mat.append(line)
# print("Matrix = ", mat, file=sys.stderr, flush=True)

# Store the coordinates of the nodes with 0 (power cells) in mat_0
mat_0 = []
for i in range(height):
    for j in range(width):
        if mat[i][j] == '0':
            mat_0.append([j,i])
            # print(mat[i][j], file=sys.stderr, flush=True)
print("Matrix of 0 = ", mat_0, file=sys.stderr, flush=True)

nodes = len(mat_0)
# print("Nodes = ", nodes, file=sys.stderr, flush=True) 
sol = ""
for i in range(nodes):
    node_x = mat_0[i][0]
    node_y = mat_0[i][1]
    sol = sol + str(node_x) + " " + str(node_y) + " "
    if nodes == 1:
        sol = str(node_x) + " " + str(node_y) + " " + "-1 -1 " + "-1 -1 "
        break
    x_found = 0
    y_found = 0
    # print("Pending nodes = ", mat_0[i:], file=sys.stderr, flush=True)
    m = 0
    l = 0
    for j in range(m+1,nodes):
        next_x = [node_x+j,node_y]
        # print("next node x = ", next_x, file=sys.stderr, flush=True)
        # print("solus = ", sol, file=sys.stderr, flush=True)
        if next_x in mat_0 and x_found == 0:
            # print("Next", file=sys.stderr, flush=True)
            sol = sol + str(next_x[0]) + " " + str(next_x[1]) + " "
            # print("solus x = ", sol, file=sys.stderr, flush=True)
            x_found = 1
            break
        elif j == nodes - 1 and x_found == 0:
            sol = sol + "-1 -1 "
        m = m + 1
    # print("x found = ", x_found, file=sys.stderr, flush=True)
    for k in range(l+1,nodes):
        next_y = [node_x,node_y+k]
        # print("next node y = ", next_y, file=sys.stderr, flush=True)
        # print("solus = ", sol, file=sys.stderr, flush=True)
        if next_y in mat_0 and y_found == 0:
            sol = sol + str(next_y[0]) + " " + str(next_y[1]) + " "
            # print("solus y = ", sol, file=sys.stderr, flush=True)
            y_found = 1
            break
        elif k == nodes - 1 and y_found == 0:
            sol = sol + "-1 -1 "
        l = l + 1
    # print("Node = ", node_x, node_y, file=sys.stderr, flush=True)
    sol = sol + "\n"
    # mat_0.remove(mat[i])
    # print("Matrix of 0 = ", mat_0, file=sys.stderr, flush=True)

# Add the -1 -1 to the last node which has by definition no neighbours
# sol = sol.rstrip("\n") + "-1 -1 " + "-1 -1 "
# print("solus = ", sol, file=sys.stderr, flush=True)

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# Three coordinates: a node, its right neighbor, its bottom neighbor
print(sol)
