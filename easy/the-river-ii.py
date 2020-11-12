def sum_digits(num):
    # Function to obtain the sum of the digits of a number
    res = 0
    lis = list(str(num))
    for i in lis:
        res = res + int(i)
    return res

# Number to be checked
# Every number is the starting point of a digital river so:
# only one more needs to be found to print "YES"
r = int(input())

# The maximum distance between each number is 9 times the length of the larger number
l = 9*len(str(r))

# Check the numbers in that interval between r-l and r
for i in range(l):
    # Current number is in position i in that interval
    num = r - i
    # Calculate the next number for num
    # No need to loop because if the new number falls into the interval it will be
    # checked in a following loop
    num += sum_digits(num)
    # If it is equal to r, a solution has been found
    if num == r:
        print("YES")
        exit()

# If none met the requirement, print "NO"
print("NO")
