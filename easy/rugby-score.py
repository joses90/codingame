# Score to be obtained
n = int(input())
# Maximum amount for each option
max_tries = n//5+1
max_transfor = max_tries
max_penalty = n//3+1

# For each possible try
for i in range(max_tries):
    # Initialise transformations
    j = 0
    # The transformations need to be less or equal than the tries
    while j <= i:
        # For each possible penalty
        for k in range(max_penalty):
            # If the score is equal to the desired n
            if (i*5+j*2+k*3) == n:
                # Print the amount for each option
                print(i,j,k)
        # Increase the transformations
        j += 1
