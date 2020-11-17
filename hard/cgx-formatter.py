# Number of lines to be read
n = int(input())
# String to store all the lines together
code=""

# Read and store the lines removing the trailing spacebars
for i in range(n):
    cgxline = input().strip()
    code += cgxline

# Initialise the counter to go trhough the string
j = 0
# List to store the different groups encountered
lis = []
# Separators that change the expected behaviour
separators = ["(",")",";"]
# String variable to store current string value
s = ""
# 0 if current cahracter is inside two apostrophes, 0 if outside
apostrophe = 0

# If there are no parenthesis
if "(" not in code:
    # Look through the string
    while j < len(code):
        # If an apostrophe is found, update the coresponding variable
        if code[j] == "'":
            apostrophe = 1 - apostrophe
        
        # If there is a semicolon or is the last character and we are
        # not inside apostrophes
        if (code[j] == ";" or j == len(code)-1) and apostrophe == 0:
            # Update the string value, print it and restart it
            s += code[j]
            print(s)
            s = ""
        # Ignore spaces and tabs outside apostrophes
        elif (code[j] == " " or code[j] == "\t") and apostrophe == 0:
            pass
        # Otherwise, update the string   
        else:
            s += code[j]
        
        # Go to the next character
        j += 1

    # Exit code if no parentheses appear
    exit()

# If there are parentheses
else:
    # Look through the string
    while j < len(code):
        # If an apostrophe is found, update the coresponding variable
        if code[j] == "'":
            apostrophe = 1 - apostrophe

        # If the character is a parenthesis or the semicolon and we are
        # not inside apsotrophes      
        if code[j] in separators and apostrophe == 0:
            # If the string is not empty
            if s != "":
                # Add that string to the list and restart it
                lis.append(s)
                s = ""
            # Add the separator as the next component in the list
            lis.append(code[j])
        # Ignore spaces and tabs outside apostrophes
        elif (code[j] == " " or code[j] == "\t") and apostrophe == 0:
            pass
        # Otherwise, update the string 
        else:
            s += code[j]
        
        # Go to the next character
        j += 1

    # If the list is empty, add the string found to it
    if lis == []:
        lis.append(s)

# Variable to store the number of spaces required to indent each line
indent = 0

# Look through the list
for k,val in enumerate(lis):
    # Variable to check if the next character is a semicolon
    add_semi = 0

    # If the character is not the last one
    if k < len(lis) - 1:
        # Update the semicolon variable if the next one is
        if lis[k+1] == ";":
            add_semi = 1
    
    # Ignore the semicolon value (to be added in other cases)
    if val == ";":
        pass
    # If the character is "(" print its indented line an update the indent
    elif val == "(":
        print(" "*indent + val)
        indent += 4
    # Similar with ")"
    elif val == ")":
        # Update the indent
        indent -= 4
        # If the next one is a semicolon, print its line and restart add_semi
        if add_semi == 1:
            print(" "*indent + val + ";")
            add_semi = 0
        # Otherwise, print the indented line
        else:
            print(" "*indent + val)
    # If the character is not "(", ")" or ";", similar to the previous example
    else:
        if add_semi == 1:
            print(" "*indent + val + ";")
            add_semi = 0
        else:
            print(" "*indent + val)
