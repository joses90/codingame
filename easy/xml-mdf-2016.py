# Extract the maximum weight for the list of tags
def max_weight(dic):
    # Look through the dictionary of tags
    for i in dic:
        # Substitute the value for the weight
        dic[i] = sum([1/j for j in dic[i]])

    # Initialise the maximum weight value and the solution
    maxs = 0
    res = ""

    # Look through the dictionary of tags
    for i in dic:
        # If the weight is greater than the actual maximum
        if dic[i] > maxs:
            # Update the maximum and the greatest weight tag name
            maxs = dic[i]
            res = i
        # If the weight is the same as the actual maximum
        # and the tag is alphabetically before the current one
        elif dic[i] == maxs and i < res:
            # Update the greatest weight tag name
            res = i

    # Return the solution
    return res

# Store the sequence to analyse
sequence = input()

# Initialise the dictionary to store the tags name and their depths
dic = {}
# Initialise the depth variable and the position counter
depth = 0
i = 0

# Look through the sequence
while i < len(sequence):
    # # If the character is not a "-"
    if sequence[i] != "-":
        # Increase the depth by 1
        depth += 1

        # If the tag is in the dictionary
        if sequence[i] in dic:
            # Add its new depth to value for that tag
            dic[sequence[i]].append(depth)
        # Otherwise
        else:
            # Add the tag and its depth value to the dictionary
            dic[sequence[i]] = [depth]
        i += 1
    # If it is a "-"
    else:
        # Decrease the depth by 1
        depth -= 1
        # Jump the following character and go to the next one
        i += 2

# Obtain the character with the maximum weight and print it
sol = max_weight(dic)
print(sol)
