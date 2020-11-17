# Number of characters (not used in this code)
n = int(input())
# Split characters into list
lis = input().split()

# Is there a minus sign?
# If so, activate the neg variable and remove the sign from the list and start the string
if "-" in lis:
    neg = 1
    lis.remove("-")
    s = "-"
# Otherwise, deactivate the neg variable and initialise the string to be stored
else:
    neg = 0
    s = ""

# Is there a decimal dot?
# If so, activate the dot variable and remove the dot from the list
if "." in lis:
    dot = 1
    lis.remove(".")
# Otherwise, deactivate the dot variable
else:
    dot = 0

# Turn the remaining elements of the list to integers
lis = [int(i) for i in lis]

# Number of zeros in list
zeros = lis.count(0)
# If all remaining elements are 0s, print 0 and exit the code
if len(lis) == zeros:
    print(0)
    exit()

# If the number is positive
if neg == 0:
    # Sort the numbers in descending order
    lis = sorted(lis,reverse=True)
    # Look through the list of integers
    for i,val in enumerate(lis):
        # If there was a dot, add it just before the last integer
        if i == len(lis) - 1 and dot == 1:
            s += "."
        # Add the element to the string
        s += str(val)
# If it is negative
else:
    # Sort the numbers in ascending order
    lis = sorted(lis)
    # Look through the list of integers
    for i,val in enumerate(lis):
        # Add the element to the string
        s += str(val)
        # If there was a dot, add it just after the first integer
        if i == 0 and dot == 1:
            s += "."

# Turn the string to a float number
num = float(s)

# If any of the following happens, round the number
# - there was not a dot
# - there was a dot, the number is positive AND there is at least one zero
if dot == 0 or (dot == 1 and neg == 0 and zeros > 0):
    num = round(num)

# Print the solution
print(num)
