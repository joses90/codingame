# Integer to check
n = int(input())

# Change subject of equation to x to see the limits of y for each n
# Starts at n+1 and ends at n*2
# Look through the possible values of y
for i in range(n+1,n*2+1):
    # If using i for y, x is an integer
    if (i*n)%(i-n) == 0:
        # Print the solution
        print(f"1/{n} = 1/{(i*n)//(i-n)} + 1/{i}")
