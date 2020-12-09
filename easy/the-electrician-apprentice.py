# For a certain equipment wiring and the switches statuses
# Return True if equipment is ON, otherwise, False
def wire(val,switchs):
    # Initialise counter of wiring for this equipment
    i = 0

    # Initialise list with switch statuses
    lis = []
    # Look through the wirings
    while True:
        # If the end of the wiring has not been reached
        if i < len(val):
            # If there is going to be parallel components
            if val[i] == "=":
                # Check the 1st paralleled component
                i += 1
                # Initialise the list of parallel components
                part = []

                # If the end of the wiring has not been reached
                # and the wiring is not a "=" or a "-"
                while i < len(val) and val[i] not in "=-":
                    # Add that component to the part list
                    # and go to the next component
                    part.append(switchs[val[i]])
                    i += 1

                # If all of the components in this part are ON
                if not any(part):
                    # The equipment will be OFF
                    return False
            # If there is going to be series components
            elif val[i] == "-":
                # Go to the next component
                i += 1
            # If it is a component in series
            else:
                # If any of them is OFF
                if not switchs[val[i]]:
                    # The equipment will be OFF
                    return False
                # If the function has not returned False at the moment,
                # go to the next component
                i += 1
        # Otherwise, if the end has been reached
        else:
            # The equipment will be ON
            return True

# Number of circuits
c = int(input())
# Initialise dictionay of equipments and switches
equipment = {}
switchs = {}

# Look through the wirings
for i in range(c):
    # Split the input
    wiring = input().split()
    # Add the equipment and its wiring to the equipment dictionary
    equipment[wiring[0]] = wiring[1:]

    # Look through the wiring
    for j in wiring[1:]:
        # Find the switches that are not already in the switchs dictionary
        if j not in switchs and j not in "-=":
            # Add the switch and False(meaning it is OFF) to the dictionary
            switchs[j] = False

# Number of switch toggles
a = int(input())

# Look through the toggles done
for i in range(a):
    # Store the switch toggled
    switch = input()

    # If it is True, change it to False and the other way round
    if switchs[switch]:
        switchs[switch] = False
    else:
        switchs[switch] = True

# Look through the list of equipments
for i in equipment:
    # Calculate if the equipment is ON or OFF
    sol = wire(equipment[i],switchs)
    # Print the solution
    print(f"{i} is",end=" ")

    if sol:
        print("ON")
    else:
        print("OFF")
