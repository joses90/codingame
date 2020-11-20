# Number of maximum bricks in a row
x = int(input())
# Number of bricks
n = int(input())
# Initialise list of masses
masses = []
# Look through each brick and add its mass to the list
for i in input().split():
    masses.append(int(i))

# Sorted them in descending order
# By logic, the heaviest ones should be at the bottom
masses = sorted(masses,reverse=True)
# Divide the list into sublists of length x
# By logic, all non-top rows should have x bricks
wall = [masses[i:i+x] for i in range(0,len(masses),x)]

# Initialise the amount of work
work_total = 0

# Look through each row of bricks (sub-list)
for j,val in enumerate(wall,start=1):
    # The sum of the masses for row j times (L-1)
    # is the work needed for that row
    work_total += sum(val)*(j-1)

# Multiply the total by the constants and print the value with 3 decimals
work_total = 0.65*work_total
print("{:0.3f}".format(work_total))
