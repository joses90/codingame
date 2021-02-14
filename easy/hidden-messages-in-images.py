# Import module to help
import re

# Number of lines with number and the amount per line (the other way around)
w, h = [int(i) for i in input().split()]
# Initialise the list of least significant bit
stri = ""

# Look theough each line of numbers
for i in range(h):
    # Look through each number
    for j in input().split():
        # Turn the number to binary, then string and
        # add its less significant bit to the string
        stri += str(bin(int(j)))[-1]

# Divide the string into 8 bits groups
lis = re.findall("........",stri)
# Initialise the solution
sol = ""

# Look through each byte
for k in lis:
    # Convert the byte to an integer and add its ASCII value to the solution
    sol += chr(int(k,2))

# Print the solution
print(sol)
