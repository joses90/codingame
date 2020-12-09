# Math module for sin, cos and inf
import math

# Extract the radian value for a string
def degree(string):
    # Initialise solution
    sol = 0
    # Unless specified, the result is positive
    neg = 0
    # Extract N,S,E,W direction
    dire = string[0]
    # Extract the numbers for the position
    degrees = string[1:]

    # If it is a latitude
    if dire in "NS":
        # Lat > 0: N, Lat < 0: S
        if dire == "S":
            neg = 1
        # Extract the defrees, arcminutes and arcseconds
        degr = float(degrees[:2])
        minu = float(degrees[2:4])
        seco = float(degrees[4:])
    # If it is a longitude
    elif dire in "EW":
        # Lon > 0: E, Lon < 0: W
        if dire == "W":
            neg = 1
        # Extract the defrees, arcminutes and arcseconds
        degr = float(degrees[:3])
        minu = float(degrees[3:5])
        seco = float(degrees[5:])

    # Obtain the value of the angle in radians
    sol = (degr + minu/60 + seco/3600)*math.pi/180

    # If needed, change the sign
    if neg == 1:
        sol = -sol

    # Return the solution
    return sol

# Number of capitals
n = int(input())
# Number of geolocations to check closest capital
m = int(input())
# Earth's radius
r = 6371
# Initialise lists for capitals, their latitudes, longitudes and messages
capitals = [""]*n
cap_lat = [0]*n
cap_lon = [0]*n
message = [0]*n

# Look through every capital
for i in range(n):
    # Extract the name and radian values for its lat and long
    lis = input().split(" ")
    capitals[i] = lis[0]
    cap_lat[i] = degree(lis[1])
    cap_lon[i] = degree(lis[2])

# Store the value for each message
for i in range(n):
    message[i] = input()

# Look through every geolocation
for i in range(m):
    # Extract the radian values for lat and long
    travel_geoloc = input().split(" ")
    lat2 = degree(travel_geoloc[0])
    lon2 = degree(travel_geoloc[1])
    # Initialise the minimum distance
    mins = math.inf
    # Initialise the solution
    equals = []

    # Look through every capital
    for j, val in enumerate(message):
        # Store the value for lat and long
        lat1 = cap_lat[j]
        lon1 = cap_lon[j]
        # Obtain the distance between the geolocation i and capital j
        dis = round(r*math.acos(math.sin(lat1)*math.sin(lat2)+math.cos(lat1)*math.cos(lat2)*math.cos(lon2-lon1)))

        # If the distance is less than the current minimum
        if dis < mins:
            # Update the minimum
            mins = dis
            # Restart the solution with the message for the capital j
            equals = [message[j]]
        # Else, if the distance is equal to the current minimmum
        elif dis == mins:
            # Add the message for capital j to the solution
            equals.append(message[j])
    
    # Print the solution/s for capital j
    print(*equals)
