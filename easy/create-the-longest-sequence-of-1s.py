# To help group by characters
from itertools import groupby

# String with the 0s and 1s
b = input()

# Separate into a list the characters i.e. each group of 0s/1s into one element
c = ",".join("".join(group) for key, group in groupby(b)).split(",")

# If only ones or zeros appear and not both
if len(c) == 1:
    # If it is 0s, print 1
    if  c[0][0] == "0":
        print(1)
    # If it is 1s, print the number of ones
    else:
        print(len(c[0]))
    # Finish the code
    exit()

# Initialise a list
d = []

# For every group
for i in c:
    # If it is a group of 1s, add to the list the number of ones in that group
    if i[0] == "1":
        d.append(len(i))
    # If it is zeros, add the string containing the 0s
    else:
        d.append(i)

# Initialise the counter, the maximum value, and the original length
j = 0
maxs = 0
length = 0

# For each element except the last two
while j < len(d)-2:
    # If the current cell is an integer i.e. number of ones
    if isinstance(d[j],int):
        # The current length is updated
        length = d[j]
        # One zero can be switched in the next string
        length += 1
        
        # However, if the next one is more than one zero,
        # the count can be stopped for this part, and jump to the next int
        if len(d[j+1]) > 1:
            j += 2
        # On the other hand, if it is just one 0, the length increases with the next int
        else:
            length += d[j+2]
            j += 2
    # Since for the rest of the cases, it jumps from int to int, this will only apply
    # if the first one is a group of zeros
    else:
        j += 1
    
    # If the current length is larger than the maximum value, update maxs
    if length > maxs:
        maxs = length

# Check if the last group is an integer and its length plus one from the previous 0
# is larger than the maximum value
if isinstance(d[-1],int) and d[-1] + 1 > maxs:
    maxs = d[-1] + 1

# Print the result for strings with more than one group
print(maxs)
