import sys
# What is the name of digit d?
def digit(d):

    d = int(d)
    dic = {0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}

    return dic[d]

# What is the name of number n (between 10 and 19 included)?
def teen(n):

    n = int(n)
    dic = {10:"ten",11:"eleven",12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}

    return dic[n]

# What is the name of the decade starting with number n?
def tens(n):

    d = int(n[0])
    dic = {2:"twenty",3:"thirty",4:"forty",5:"fifty",6:"sixty",7:"seventy",8:"eighty",9:"ninety"}

    return dic[d]

# Which separators do we need for a number that is divided in l groups of 3 digits?
def separ(l):

    lis = ["thousand","million","billion","trillion","quadrillion","quintillion"]
    return lis[:l-1]

# What is the number without zeros on the left for number n (3 digits at most)?
def number_reduce(n):

    if len(n) == 1:
        num = n
    elif n[0] == "0":
        if n[1] == "0":
            if n[2] == "0":
                return ""
            else:
                num = n[2]
        else:
            num = n[1:]
    else:
        num = n

    return num

# Convert a three/two/one digits number into its name
def convert2letter(num):

    # Initialise the solution
    sol = ""
    # If there is no number (it comes from a 000 from number_reduce), return "empty"
    if num == "":
        sol = "empty"
    # Otherwise
    else:
        # If the number is above 99
        if len(num) == 3:
            # Update the solution with the digit for the hundred and "hundred"
            sol += digit(num[0]) + " hundred"
            # Remove the hundred digit already considered
            num = num[1:]
        # If the current number is between 00 and 99 included
        if len(num) == 2:
            # If the there was a hundred digit or there are no decade and unit numbers
            if sol == "" or num == "00":
                pass
            # Otherwise
            else:
                # Add a space to the solution to separate the hundreds from the tens
                sol += " "
            # If the decade digit is 0
            if num[0] == "0":
                # If the unit digit is not 0
                if num[1] != "0":
                    # Update the solution with the text for the digit
                    sol += digit(num)
            # If the decade number is 1
            elif num[0] == "1":
                # Update the solution with the text for the teen number
                sol += teen(num)
            # Otherwise, if the number is between 20 and 99
            else:
                # Update the solution with the text for the decade digit
                sol += tens(num)
                # If the unit digit is not 0, update the solution with
                # the hyphen and the text for the unit digit
                if num[1] != "0":
                    sol+= "-" + digit(num[1])

        # If the number is between 0 and 9 included, update the solution
        # with the text for the unit digit
        if len(num) == 1:
            sol += digit(num[0])

    # Return the solution
    return sol

# Count of numbers to be translated to english
n = int(input())

# Look through each number/ line
for i in range(n):
    # Number to be translated
    x = input()
    # Initialise variable to check if the number is negative
    neg = 0
    # If the number is negative, update the variable and remove the sign
    if x[0] == "-":
        neg = 1
        x = x[1:]
    
    # Convert the string number into a list of strings with one element per
    # group of 3 (thousand separators)
    x = str(f"{int(x):,}").split(",")

    # Invert the list to ease the process
    inv = x[::-1]
    print("x:   ",x, file=sys.stderr, flush=True)
    print("inv:   ",inv, file=sys.stderr, flush=True)
    # Initialise variables to store the reduced numbers for each group,
    # the english translation for each one
    # and the separators needed
    group3 = []
    letters = []
    separators = []

    # Look through each group
    for j in range(len(inv)):
        print("j:   ",j, file=sys.stderr, flush=True)
        # Remove the leading zeros
        group3.append(number_reduce(inv[j]))
        # Translate to english
        letters.append(convert2letter(group3[j]))
        print("current group:   ",group3[j], file=sys.stderr, flush=True)
        # Obtain the separators
        separators = separ(len(inv))

    print("letters:   ",letters, file=sys.stderr, flush=True)
    print("separators:   ",separators, file=sys.stderr, flush=True)

    # Initialise the result variable and a counter
    result = []
    k = 0

    # Look through the translations for each group
    while k < len(letters):
        # Add it to the result
        result.append(letters[k])
        # Next, add the separator if it is not the last element of translations
        if k < len(separators):
            result.append(separators[k])
        # Update the counter
        k += 1

    # Invert the solution    
    result = result[::-1]
    print("result:                  ",result, file=sys.stderr, flush=True)
    # Initialise a counter for strings considered
    h = 0
    # Look through the strings in the solution
    while h < len(result):
        # If it is empty, remove it from the list
        if result[h] == "empty":
            result.pop(h)
            # Also, if the string was not the last one, remove the
            # separator that follows it
            if h < len(result) - 1:
                result.pop(h)
        # Otherwise, check the next element
        else:
            h += 1
    # If the number was negative, add the corresponding text at the beginning
    if neg == 1:
        result.insert(0,"negative")
    # Print the result
    print(*result)
