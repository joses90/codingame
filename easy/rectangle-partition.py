# Import counter to help merging dictionaries
from collections import Counter

# Width and height of rectangle
# Also, measurements for dividers in x and y
w, h, count_x, count_y = [int(i) for i in input().split()]
# Initialise dictionary with width and height as the first submeasurements.
# The value of these keys/submeasurements is one as they only appear once
w_x = {w:1}
w_y = {h:1}

# Input every x divider width
for i in input().split():
    x = int(i)
    # Add it to the dictionary with a value of one repetition
    w_x[x] = 1

# Initialise the dictionary to compute the subwidths resulting from the difference
# between the x dividers written before
sub_x = {}

# Loop through the x dividers dictionary twice
for i in w_x:
    for j in w_x:
        # Since the search will be simmetrical and the diagonal is zero, we can reduce
        # the look to one half
        if i < j:
            # Obtain the abs difference of the subwidths
            a = abs(i-j)
            # If the value is already in the dictionary of subwidths, increment its repetition
            if a in sub_x:
                sub_x[a] += 1
            # If it is not, include it in the dictionary
            else:
                sub_x[a] = 1

# Similar behaviour as with the width/subwidths for the height/subheigths
for i in input().split():
    y = int(i)
    w_y[y] = 1

sub_y = {}

for i in w_y:
    for j in w_y:
        if i < j:
            a = abs(i-j)
            if a in sub_y:
                sub_y[a] += 1
            else:
                sub_y[a] = 1

# For each dimension, "sum" the dimensions and subdimensions dictionaries into one
x = dict(Counter(w_x)+Counter(sub_x))
y = dict(Counter(w_y)+Counter(sub_y))

# For each one of them, since dictionaries cannot be sorted by key, convert it to
# an ordered tuple dimension_sorted
items_x = x.items()
x_sorted = sorted(items_x)
items_y = y.items()
y_sorted = sorted(items_y)

# Initialise the count of squares found
count = 0
# Look for each different value in x
for i in x_sorted:
    # Look for each different value in y
    for j in y_sorted:
        # Only if the value of one of the dimensions is lower or equal than the other
        if i[0] <= j[0]:
            # If they are equal, add the product of their repetitions to the counter
            if i[0] == j[0]:
                count += i[1]*j[1]
            # NEED to recheck why did I write this ???
            break

# Print the result
print(count)
