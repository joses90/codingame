import math

# Does the motorcycle with speed v falls at curve with raidus r?
def fall_m(v,r):
    # Gravity
    g = 9.81
    # VERTICAL angle in degrees
    angle = math.atan((v**2)/(r*g))*(180/math.pi)

    # Returns True if the VERTICAL angle is larger than 60
    # i.e. the motorcycle falls
    if angle > 60:
        return True
    else:
        return False

# What is the optimal (as an integer) speed to not fall in any curve?
def optimal_speed(curves):

    # Critical angle to fall
    angle = 60*math.pi/180
    # Gravity
    g = 9.81
    # Critical curve
    r = min(curves)
    # Optimal speed
    opt = math.sqrt(r*g*math.tan(angle))
    # Converted to an integer
    opt = math.floor(opt)

    # Return optimal speed
    return opt

# Number of motorcycles (mine not included)
n = int(input())
# Number of curves
v = int(input())
# Dictionary to store the speed for each motorcycle
speed = {}
# List to store the radius of each curve
curves = []
# List to store the speeds that will be used to sort them
lis_speed = []

# Look through all motorcycles
for i in range(n):
    # Input its speed
    sp = int(input())
    # Store the motorcycle as a key and its speed as a value
    speed[chr(i+97)] = sp
    # Add the speed to the list of speed
    lis_speed.append(sp)

# Look through the curves and add them to the list
for i in range(v):
    curves.append(int(input()))

# Calculate my speed and add it to the dictionary and list
my_speed = optimal_speed(curves)
speed["y"] = my_speed
lis_speed.append(my_speed)

# Sort the list of speeds in reverse order
# If there were no curves, this is the order they would arrive at the end
lis_speed = sorted(lis_speed,reverse=True)
# Initialise list of motorcycles that will not fall in any of the curves
fall = []
# Similar for those that fall in at least one
no_fall = []

# Look through the list of speeds
for i in lis_speed:
    # Get the motorcycle letter for the current speed
    key = list(speed.keys())[list(speed.values()).index(i)]

    # If the speed is lower or equal than mine, they will not fall at any point
    if i <= my_speed:
        # By storing it in a different list, we avoid checking for these
        # motorcycles at every curve (we know they will not fall)
        no_fall.append(key)
    # Otherwise, they will fall once at least
    else:
        fall.append(key)

# Look through every curve
for curve in curves:
    # Index for motorcycle
    i = 0
    # Counter of number of motorcycles already considered
    j = 0

    # Check if the motorcycles have been all counted
    while j < len(fall):
        # Speed for that motorcycle
        vel = speed[fall[i]]

        # Check if it falls (True) or not (False)
        if fall_m(vel,curve):
            # Remove the motorcycle from the list and add it to the end
            change = fall.pop(i)
            fall.append(change)
        # If it does not fall, do not do anything and check the next one
        else:
            i += 1
        
        # Increase the number of motorcycles counted
        j += 1


# Print my speed
print(my_speed)

# Print first the motorcycles that do not fall in descending speed order
for i in no_fall:
    print(i)

# Print the list of motorcycles that have fallen at least once
for j in fall:
    print(j)
