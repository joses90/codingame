# Number of tributes
tributes = int(input())
# Store the tributes' names
tribute_list = []
# Dictionary to store who (values) has been killed by whom (keys)
kill = {}

# Look through the tributes and store them
for i in range(tributes):
    tribute_list.append(input())

# Sort alphabetically the tributes
tribute_list = sorted(tribute_list)

# For now, each tribute has not killed anyone
for i in tribute_list:
    kill[i] = []

# Number of turns
turns = int(input())

# Look through each turn/line
for i in range(turns):
    # Read the info, removing the commas and splitting into a list
    info = input().replace(",","").split()
    # The killer is the first element
    # The second one is the word "killed" which is not going to be used
    killer = info[0]
    # Store the list of people to be killed by this killer
    killed = info[2:]

    # Add every person killed to the list for that killer
    for j in killed:
        kill[killer].append(j)

# Look throug each killer
for k in kill:
    # Print the name of the current tribute
    print("Name:",k)
    
    # If k has not killed anyone (his/her list is empty)
    if not kill[k]:
        print("Killed:","None")
    # If k has killed other tributes, sort them and
    # print them separated by commas
    else:
        killed_by = sorted(kill[k])
        print("Killed:",", ".join(killed_by))

    # Variable to see if k has won (not been killed)
    winner = 1

    # Look through every killer
    for t in kill:
        # If k has been killed t, print his/her name
        # update the winner variable and exit the loop
        # since nobody can be killed twice
        if k in kill[t]:
            print("Killer:",t)
            winner = 0
            break
    
    # If k has not been killed, k is the winner
    if winner == 1:
        print("Killer:","Winner")

    # If k is not the last tribute, print an empty line
    if k != tribute_list[-1]:
        print()
