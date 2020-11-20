import math
# Number of quadrilaterals
n = int(input())

# Look through each quadrilateral
for i in range(n):
    # Input the name and coordinates for each vertex
    a, x_a, y_a, b, x_b, y_b, c, x_c, y_c, d, x_d, y_d = input().split()
    # Turn the values to integers
    x_a = int(x_a)
    y_a = int(y_a)
    x_b = int(x_b)
    y_b = int(y_b)
    x_c = int(x_c)
    y_c = int(y_c)
    x_d = int(x_d)
    y_d = int(y_d)

    # Obtain the length of each side into ist x and y components
    x2,y2 = x_b-x_c,y_b-y_c
    x3,y3 = x_c-x_d,y_c-y_d
    x4,y4 = x_d-x_a,y_d-y_a

    # Obtain the length of two consecutive sides
    l3 = math.sqrt(x3**2+y3**2)
    l4 = math.sqrt(x4**2+y4**2)

    # Print the name of the quadrilateral
    print(a+b+c+d + " is a ",end="")

    # Initialise the values that check if it is a rhombus or a rectangle
    rhombus = 0
    rectangle = 0

    # If opposites sides are equal, it cannot be an "irregular" quadrilateral
    if abs(x2) == abs(x4) and abs(y2) == abs(y4):
        # If consecutives sides have equal length, it is at least a rhombus
        if l3 == l4:
            rhombus = 1

        # If the dot product of consecutive sides is 0, it is at least a rectangle
        if x3*x4 + y3*y4 == 0:
            rectangle = 1

        # If it is a rhombus
        if rhombus == 1:
            # And not a rectangle, it is a rhombus
            if rectangle == 0:
                print("rhombus.")
            # And a rectangle, it is a square
            elif rectangle == 1:
                print("square.")
        # If it is not, but it is a rectangle, it is a rectangle
        elif rectangle == 1:
            print("rectangle.")
        # Otherwise, it is a parallelogram
        else:
            print("parallelogram.")
    # Otherwise, it is a quadrilateral
    else:
        print("quadrilateral.")
