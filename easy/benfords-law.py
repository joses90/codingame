# Initialise the dictionary with the count of leading numbers
dic = {str(i):0 for i in range(1,10)}
# Configure the benford law percentages dictionary
benford = {"1":0.301,"2":0.176,"3":0.125,"4":0.097,"5":0.079,"6":0.067,"7":0.058,"8":0.051,"9":0.046}

# Number of transactions
n = int(input())

# Look through each line/transaction
for i in range(n):
    # Store the transaction string without spaces
    transaction = input().replace(" ","")
    # Initialise a counter
    j = 0
    # Initialise the leading number
    leading = transaction[j]

    # Look for the first character that is a number and different from 0
    # and store it in the leading variable
    while not transaction[j].isnumeric() or transaction[j] == "0":
        j += 1
        leading = transaction[j]

    # Increase the ocurrences of this leading number in the dictionary
    dic[leading] += 1

# Look through each leading number
for j in dic:
    # Update each entry with its percentage of the total of transactions n
    dic[j] = dic[j] / n

    # If the percentage is more than 10% outside the Benford law percentages,
    # the account is irregular, print "true" and exit the code
    if dic[j] < benford[j] - 0.1 or dic[j] > benford[j] + 0.1:
        print("true")
        exit()

# If no error has been encountered, the account is regular
print("false")
