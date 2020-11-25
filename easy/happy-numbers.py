# Amount of numbers to be tested
n = int(input())

# For every number
for i in range(n):
    # Input the number
    x = input()
    # Print the number
    print(x,end=" ")
    # Remove 0s as they will not change the result
    x = x.replace("0","")

    # Loop until there is a single digit
    while True:

        # If there is a single digit
        if len(x) == 1:
            # If it is 1 or 7, it is a happy number (check by yourself)
            if x in ("1","7"):
                print(":)")
            # Otherwise, it is an unhappy number
            else:
                print(":(")
            # Either way, the loop finishes and we can check the next one
            break
        # If there are more digits
        else:
            # Transform the number into a list (one digit per element)
            lis = list(x)
            # Initialise the resulting number
            num = 0
            
            # For each digit in the list
            for j in lis:
                # Add the square of that number to the resulting number
                num += int(j)**2
            
            # Transform it to a string to be used in the next iteration
            x = str(num)
