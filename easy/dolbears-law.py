# Number of minutes
m = int(input())
# Initialise list with measurements
msrmnts = []

# For each minute
for i in range(m):
    # Store in a list the number of chirps every 4 second
    line = input().split()
    # Transform each element into an integer
    line = [int(i) for i in line]
    # Add the values to the list
    msrmnts.extend(line)

# Divide into sublists with 15 measurements (60 seconds) per sublist
n60_list = [msrmnts[i:i + 15] for i in range(0, len(msrmnts), 15)]
# Obtain the amount of chirps every 60 seconds
n60_sum = [sum(i) for i in n60_list]
# Obtain the rounded estimate for the temperature
# from the average of chirps per 60 seconds
t60 = round(10 + (sum(n60_sum)/len(n60_sum) - 40) / 7,1)

# Print the first result
print(t60)

# If the value is within certain range
if 5 <= t60 <= 30:
    # Remove the last measurement if teh count is odd
    if len(msrmnts) %2 == 1:
        msrmnts.pop()
    
    # Divide into sublists with 2 measurements (8 seconds) per sublist
    n8_list = [msrmnts[i:i + 2] for i in range(0, len(msrmnts), 2)]
    # Obtain the amount of chirps every 8 seconds
    n8_sum = [sum(i) for i in n8_list]
    # Obtain the rounded estimate for the temperature
    # from the average of chirps per 8 seconds
    t8 = round((sum(n8_sum)/len(n8_sum) + 5),1)
    
    # Print the second result
    print(t8)
