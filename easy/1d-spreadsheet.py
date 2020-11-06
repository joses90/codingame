# Number of cells
n = int(input())
# Dictionary to store cell number as key and rest of inputs as values
dic = {}
# Store inputs into dictionary
for i in range(n):
    dic[i] = input().split()
    # If the operation is VALUE and the number does not contain a reference,
    # update the dictionary value to be the int of that number
    if dic[i][0] == "VALUE" and dic[i][1][0] != "$":
        dic[i] = int(dic[i][1])

# Store cells that are already integers
solved = []
# Look until all cells values are integers
while len(solved) < n:
    # Look through dictionary
    for key in dic:
        # If the value is a dictionary (not a list)
        if isinstance(dic[key],int):
            # If the cell has not been included already in the integer cells list
            if key not in solved:
                # Add it to the list
                solved.append(key)
        # If it is a list
        # and the second argument is an integer
        # and the third argument is an integer
        elif isinstance(dic[key][1],int) and isinstance(dic[key][2],int):
                # If the first argument is "ADD", the new dictionary value is the sum
                if dic[key][0] == "ADD":
                    dic[key] = dic[key][1] + dic[key][2]
                # If the first argument is "SUB", the new dictionary value is the substraction
                elif dic[key][0] == "SUB":
                    dic[key] = dic[key][1] - dic[key][2]
                # If the first argument is "MULT", the new dictionary value is the multiplication
                elif dic[key][0] == "MULT":
                    dic[key] = dic[key][1] * dic[key][2]
        # If it is a list
        # and the second argument is an integer
        # and the first argument is equal to "VALUE"
        elif isinstance(dic[key][1],int) and dic[key][0] == "VALUE":
                # The new dictinary value is that value
                dic[key] = dic[key][1]
        # If it is a list not covering the previous cases
        else:
            # If the second argument is a string
            if isinstance(dic[key][1],str):
                # If the second argument starts with a "$"
                if dic[key][1][0] == "$":
                    # If the number following the "$" is in the integer cells list
                    if int(dic[key][1][1:]) in solved:
                        # SUBSTITUTE the second argument with the value for the cell referenced
                        dic[key][1] = dic[int(dic[key][1][1:])]
                # If the second argument is not "_"
                elif dic[key][1][0] != "_":
                    dic[key][1] = int(dic[key][1])
            # Same as previous IF, except for the third argument
            if isinstance(dic[key][2],str):
                if dic[key][2][0] == "$":
                    if int(dic[key][2][1:]) in solved:
                        dic[key][2] = dic[int(dic[key][2][1:])]
                elif dic[key][2][0] != "_":
                    dic[key][2] = int(dic[key][2])

# Print each result for each cell
for cell in dic:
    print(dic[cell])
