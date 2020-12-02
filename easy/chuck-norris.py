# Import groupby to help divide the binary string into chunks
# Each one has 0s or 1s but not both
from itertools import groupby
# Input the message
message = input()
# Initialise the binary message
bin01 = ""

# Look through every character
for x in message:
    # Format it to its 7-bits binary form and add it to the string of 0s and 1s
    bin01 += ("".join(format(ord(x),"b"))).zfill(7)


# Calculate length of string
l = len(bin01)
# Initialise the string  of 0s and a counter
bin0 = ""

# Look through every group of same consecutive numbers
for k,chunk in groupby(bin01):
    # How many are there in each chunk?
    amount = len("".join(chunk))

    # If it is a group of 0s, add "00 "
    if k == "0":
        bin0 += "00 "
    # If it is a group of 1s, add "0 "
    elif k == "1":
        bin0 += "0 "
    
    # Add the amount of zeros needed for this group
    bin0 += "0"*amount + " "

# Print the solution without the final space
print(bin0[:-1])
