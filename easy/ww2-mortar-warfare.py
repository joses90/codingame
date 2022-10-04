# To use periodic functions and pi
import math

# Distance to target with additional characters and initalise range
n = input()
R=""

# Check if the characters are numbers
for i in str(n):
    # If they are, add them to the range variable
    if i.isnumeric():
        R+=i

# Convert range to integer and detail gravity and initial velocity
R = int(R)
v0 = 158
g = 9.8

# If the target is out of range (too far)
if R > 1800:
    print("OUT OF RANGE")
else:
    # Obtain angle to reach the specified range
    angle = ((math.asin((R*g)/(v0**2)))/2)*180/math.pi
    # If the angle is not between 40 and 85, obtain its complementary
    if angle < 40 or angle > 85:
        angle = 90 - angle
        # If the complementary is still not in that interval, the target is too close
        if angle < 40 or angle > 85:
            print("OUT OF RANGE")
        else:
            # If it is in range, obtain the time to reach the target and print the results
            t = (2*v0*math.sin(angle*math.pi/180)/g)
            print("%.1f" % angle + " degrees")
            print("%.1f" % t + " seconds")
