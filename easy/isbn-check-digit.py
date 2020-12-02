# Amount of ISBN to check
n = int(input())
# Initialise list with invalid ISBN
invalid = []

# Look through every ISBN
for i in range(n):
    # Divide into a list
    ISBN = list(input())
    # Restart the variable to calculate which is the last digit needed
    num = 0

    # If the ISBN has been invalidated already, skip it
    if "".join(ISBN) in invalid:
        pass
    # If any of the characters (except the last one) is not a number
    # or the length of the ISBN is not 10 or 13, this ISBN is invalid 
    elif not "".join(ISBN[:-1]).isnumeric() or len(ISBN) not in (10,13):
        invalid.append("".join(ISBN))
    # If the ISBN has 10 digits
    elif len(ISBN) == 10:
        # Invert the list of digits
        digits = ISBN[::-1]
        # Store the last digit
        last = digits[0]

        # Convert the digits to integers (not including the last one)
        digits = [int(i) for i in digits[1:]]

        # Look through every digit and add its value times its weight
        for j,val in enumerate(digits):
            num += (j+2)*val
        # Calculate the modulus 11
        num = num % 11
        # If the last character is an "X"
        if last == "X":
            # And the calculated variable is not 1, it is an invalid ISBN
            if num != 1:
                invalid.append("".join(ISBN))
        # If the last digit is a 0
        elif last == "0":
            # And the calculated variable is not 0, it is an invalid ISBN
            if num != 0:
                invalid.append("".join(ISBN))
        # If the last digit is a number
        elif last.isnumeric():
            # And the sum of the calculated variable and this last digit
            # is not 11, it is an invalid ISBN
            if num + int(last) != 11:
                invalid.append("".join(ISBN))
        # Otherwise, it is an invalid ISBN
        else:
            invalid.append("".join(ISBN))
    # If the ISBN has 13 digits
    elif len(ISBN) == 13:
        # Store the last digit
        last = ISBN[-1]

        # If the last digit is a number
        if last.isnumeric():
            # Convert the last number to an integer
            last = int(last)
            # Convert the digits to integers (not including the last one)
            digits = [int(i) for i in ISBN[:-1]]

            # Look through every digit
            for j,val in enumerate(digits):
                # Add its value if it is an even index
                if j % 2 == 0:
                    num += val
                # Otherwise, its value times 3
                else:
                    num += val*3
            
            # Calculate the modulus 10
            num = num % 10

            # If the last digit is a 0
            if last == 0:
                # And the calculated variable is not 0, it is an invalid ISBN
                if num != 0:
                    invalid.append("".join(ISBN))
            # And the sum of the calculated variable and this last digit
            # is not 10, it is an invalid ISBN 
            elif num + last != 10:
                invalid.append("".join(ISBN))
        # Otherwise, it is an invalid ISBN
        else:
            invalid.append("".join(ISBN))

# Print the result
print(len(invalid),"invalid:")
for i in invalid:
    print(i)
