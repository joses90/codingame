# Complex number is stored
c = complex(input().replace("i","j"))
# Number of maximum iterations
m = int(input())

# Initialise counter of iteration and value of last f
i = 1
f = 0

# Loop until said
while True:
    # Apply the formula
    f = f**2 + c

    # If the absolute value is greater than 2
    if abs(f) > 2:
        # Print the iteration and exit
        print(i)
        break
    
    # Go to the next iteration
    i += 1
    
    # If the maximum amount of iterations has been reached, print m and exit
    if i == m:
        print(m)
        break
