# Square length
size = int(input())
# Number of players
n = int(input())
# Initialise list of names and scores
name = []
score = [0]*n

# Look through the names and add them to the list in appearing order
for i in range(n):
    name.append(input())

# Number of throws
t = int(input())

# Look through the throws
for i in range(t):
    # Store the player's name and the absolute value of x and y (symmetrical behaviour)
    inputs = input().split()
    throw_name = inputs[0]
    x = abs(int(inputs[1]))
    y = abs(int(inputs[2]))

    # Obtain the index for the name
    ind = name.index(throw_name)

    # If it is inside the diamond
    if y <= size/2 - x:
        # That player wins 15 points
        score[ind] += 15
    # If it is inside the circle
    elif x**2 + y**2 <= size**2 / 4:
        # That player wins 10 points
        score[ind] += 10
    # If it is inside the square
    elif x <= size/2 and y <= size/2:
        # That player wins 5 points
        score[ind] += 5

# Loop while there are scores to be printed
while score:
    # Obtain the index of the maximum score
    ind = score.index(max(score))
    # Print name and score of the remaining best player
    print(name[ind], score[ind])
    # Remove the FIRST appearance of the remaining best score and its player
    score.remove(score[ind])
    name.remove(name[ind])
