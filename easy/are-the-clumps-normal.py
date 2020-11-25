# Number to be analysed divided into digits
n = list(input())

# Initialise the amount of groups per base
# It starts at 0 although position for base 0 and 1 will not be used
db = [0 for i in range(10)]

# Start the analysis with base 2
base = 2

# Loop until certain point is reached
while True:
    # Look through the different digits
    for val in n:
        # Obtain the remainder
        rema = int(val)%base

        # If it is the first digit for that base
        if db[base] == 0:
            # The number of groups with different consecutive remainder increases
            db[base] += 1
            # The current remainder will be compared with the next one
            prev = rema
        # If it is not the first digit
        else:
            # If the last remainder and the current one are different
            if rema != prev:
                # A new group will appear
                db[base] += 1
                # The last remainde is updated
                prev = rema

    # If the number of groups is les than the one for the previous base
    if db[base] < db[base-1]:
        # Print the base number and exit the code
        print(base)
        exit()

    # If the last base is reached
    if base == 9:
        # Print Normal and exit the code
        print("Normal")
        exit()
    
    # If no deviation is found, go to the next base
    base += 1
