import math
# Function to determine the winner of each fight
def winner(p1,p2):
    # Each string contain the signs that lose to the sign mentioned in the name
    R_los,P_los,C_los,L_los,S_los= "LC","RS","PL","SP","CR"
    # If both use the same sign, the winner is the one with the lowest number
    if p1[1] == p2[1]:
        if p1[0] < p2[0]:
            win = p1
        else:
            win = p2
    # If the signs are different, the winner is determined
    elif p1[1] == "R" and p2[1] in R_los  or p1[1] == "P" and p2[1] in P_los or p1[1] == "C" and p2[1] in C_los or p1[1] == "L" and p2[1] in L_los or p1[1] == "S" and p2[1] in S_los:
        win = p1
    else:
        win = p2

    # Determine the loser
    if win == p1:
        los = p2
    else:
        los = p1

    # Return the number and sign of the winner in win and the number of the loser in los[0]
    return win, los[0]

# Number of players
n = int(input())
# Number of rounds
rounds = int(math.log2(n))
# Dictionary to store the order of the players with their number and sign
dic = {}
# Dictionary to store the number for each player defeated (list values) by which player (key)
defeated = {i: [] for i in range(1,n+1)}

# Store the players numbers and signs
for i in range(n):
    numplayer, signplayer = input().split()
    numplayer = int(numplayer)
    dic[i] = [numplayer,signplayer]

# Go through one round at a time
for j in range(rounds):
    # Counter of order of each player
    i = 0
    # Index for last in order player
    maxs = max(dic)

    # Look through the list of players
    while i < len(dic):
        # Input the list for the current player and its opponent
        # Output the winner list and the loser's number
        win,los =  winner(dic[i],dic[i+1])
        # The dictionary is updated with the winner of each fight
        # (8 players give 4 winners, 4 players give 2 winners, etc.)
        dic[i//2] = win
        # Add loser's number to winner's list
        defeated[win[0]].append(los)
        # Look for the next player to be challenged
        i += 2
    
    # Look through the new dictionary and remove the second half of key-values
    for k in range(maxs+1):
        if k > (maxs//2):
            dic.pop(k)

# Final winner
top_player = dic[0][0]
# Defeated by final winner
defe = defeated[top_player]

print(top_player)
# Print defe list as string separating by space *
print(*defe)
