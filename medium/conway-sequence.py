import sys
import math

def conv(seque):
    # If it is the first line, it is an integer and must be converted to a string
    if type(seque) == int:
        seque = str(seque)
    # Convert the line string into a list of strings
    seque_list = seque.split()
    # Convert the list of strings into a list of integers
    seque_list[:] = list(map(int, seque_list))

    return seque_list

def new_line(seque):
    # Initialise variables
    nums = []
    times = []
    i = 0

    for i in range (len(seque)):
        # Insert the first number into the list for non repeated consecutive numbers
        # Also insert 1 into the list to compute the number of times it apppears
        # The second part of the OR operator: If the current number is not the same as
        # the last one on the list, add the new number and insert 1 into the times list
        if i == 0 or seque[i] != nums[-1]:
            nums.append(seque[i])
            times.append(1)
        # If the current number is the last one on the list, increase the time number
        elif i!= 0:
            times[-1] += 1
    
    return nums, times

def new_line_string(n,t):

    # Initialise string
    sol = ""
    # Add the corresponding numbers in order
    for i in range(len(n)):
        sol += (str(t[i])+ " " + str(n[i]) + " ")

    sol = sol.strip()
    return sol

r = int(input())
l = int(input())

for k in range(1,l):

    # Convert the current line into a list
    lis = conv(r)
    # Obtain from the list the numbers (do not repeat equal consecutive)
    # and the times those numbers repeat consecutively
    numb, tim = new_line(lis)
    # Obtain the new line from the previous one
    r = new_line_string(numb,tim)

print(r)
