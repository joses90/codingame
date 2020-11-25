# Number of cards
n = int(input())

# Look through every card
for i in range(n):
    # Convert each card into a list of 16 digits
    card = [int(j) for j in list(input().replace(" ",""))]
    # First list consists of the even positioned numbers
    first = [card[j] for j in range(16) if j%2 == 0]
    # Initialise the second result
    second = 0

    # For each value in first
    for val in first:
        # Add the doubled value
        second += val*2
        # And substract nine if it has two digits
        if val*2 > 9:
            second -= 9

    # For the third step, sum all odd positioned digits
    third = sum([card[j] for j in range(16) if j%2 == 1])
    # For the fourth step, sum the two previous ones
    fourth = second + third

    # If the number is divisible by 10, it is a valid card
    if fourth % 10 == 0:
        print("YES")
    # Otherwise it is invalid
    else:
        print("NO")
