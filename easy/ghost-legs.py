# Width and height of diagram
w, h = [int(i) for i in input().split()]
# Initialise dictionary to store starter characters and the current column
# as you go downwards
mark = {}

for i in range(h):
    # Read the current line
    line = input()
    # If it is the top line T, store the characters at each column and the
    # index for each column
    if i == 0:
        for j,top in enumerate(line):
            if top != " ":
                mark[top] = j
    # If the line is not the top or bottom one
    if i < h-1:
        for j in mark:
            char = mark[j]
            # For all the columns except the one on the far right
            if char < w-1:
                # Check if there is a connector to the right and subustitute
                # the value for that column
                if line[char+1:char+3] == "--":
                    mark[j] += 3
                # Same as above for the left
                elif line[char-2:char] == "--" and char > 0:
                    mark[j] -= 3
            # Check for the rightmost column and subsitute value
            elif char == w-1:
                if line[char-2:char] == "--":
                    mark[j] -= 3
    # For the bottom line, use the values at the end of the columns to update
    # the dictionary
    else:
        for j in mark:
            mark[j] = line[mark[j]]

# Print the top-bottom pairings
for i in mark:
    print(i+str(mark[i]))
