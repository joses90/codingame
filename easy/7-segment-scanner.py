import re

# Store, per line, each digit segments as a three characters' group
l1 = re.findall("...",input())
l2 = re.findall("...",input())
l3 = re.findall("...",input())
digits = [666]*len(l1)

# For each digit
for i in range(len(l1)):
    # Top line: 0,2,3,5,6,7,8,9
    if l1[i] == " _ ":
        # Medium line: 0
        if l2[i] == "| |":
            digits[i] = "0"
        # Medium line: 2,3
        elif l2[i] == " _|":
            # Bottom line: 2
            if l3[i] == "|_ ":
                digits[i] = "2"
            # Bottom line: 3
            else:
                digits[i] = "3"
        # Medium line: 5,6
        elif l2[i] == "|_ ":
            # Bottom line: 5
            if l3[i] == " _|":
                digits[i] = "5"
            # Bottom line: 6
            else:
                digits[i] = "6"
        # Medium line: 7
        elif l2[i] == "  |":
            digits[i] = "7"
        # Bottom line: 8
        elif l3[i] == "|_|":
            digits[i] = "8"
        # Bottom line: 9
        else:
            digits[i] = "9"
    # Medium line: 1
    elif l2[i] == "  |":
        digits[i] = "1"
    # Medium line: 4
    else:
        digits[i] = "4"

# Print the combined digits
print("".join(digits))
