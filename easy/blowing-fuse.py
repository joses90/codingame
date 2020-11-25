# What is the total consumption for devices with con consumption and status sta?
def total_cons(con,sta):

    # Initialise the solution
    sol = 0

    # Look through every device
    for i, val in enumerate(sta):
        # If it is ON
        if val == True:
            # Add its consumption to the solution
            sol += con[i]
    
    # Return the total consumption
    return sol

# Input the number of devices, button-clicking actions and fuse capacity
n, m, c = [int(i) for i in input().split()]
# Initialise the list of consumptions
consumption = []
# All devices are OFF at the beginning
status = [False]*n
# Initialise the maximum value for consumption
maxs = 0

# Store the consumptions per device
for i in input().split():
    consumption.append(int(i))

# Look through the button-clicking actions
for i in input().split():
    # The actions are inputted from 1 to n, so we offset it to 0 to n-1 as saved in the other lists
    mx = int(i) - 1

    # If the device is ON, turn it OFF
    if status[mx]:
        status[mx] = False
    # If the device is OFF, turn it ON
    else:
        status[mx] = True

    # Obtain the total consumption after a single button-click
    tot_con = total_cons(consumption,status)

    # If the consumption is greater than the capacity of the fuse, the fuse is blown and the code ended
    if tot_con > c:
        print("Fuse was blown.")
        exit()
    # Otherwise, if it is larger than the current maximum
    elif tot_con > maxs:
        # Update the maximum
        maxs = tot_con

# If the fuse has not been blown, print the maximum consumption reached
print("Fuse was not blown.")
print(f"Maximal consumed current was {maxs} A.")
