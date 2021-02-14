# Width and height of image
w, h = [int(i) for i in input().split()]
# Initialise counter of Xs and matrix
x_count = 0
mat = []

# Look through each row
for i in range(h):
    # Store the row
    row = input()
    # Update the number of Xs encountered
    x_count += row.count("X")
    # Add the row to the matrix
    # Subsitute "other" characters by "X"
    mat.append([i if i in "X." else "X" for i in row])

# If the 1st and last row are equal
if mat[0] == mat[-1]:
    # And all characters are Xs
    if x_count == w*h:
        # It is a rectangle and exit the code
        print("Rectangle")
        exit()
    
    # Transpose the matrix
    mat_inv = list(map(list,zip(*mat)))

    # If the 1st and last column are equal
    if mat_inv[0] == mat_inv[-1]:
        # It is an ellipse
        print("Ellipse")
    # Otherwise, it is a triangle
    else:
        print("Triangle")
# Otherwise, it is a triangle
else:
    print("Triangle")
