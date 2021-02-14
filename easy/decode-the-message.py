# Encoded message
p = int(input())
# Alphabet used to encode and its length
c = input()
n = len(c)
# The first decoded character and the remaining number to extract
# the rest of the message
sol = c[p % n]
p //= n

# Used to check if last character in alphabet is reached
# (this control helps with the following character)
err = 0

# Loop the divisions
while True:
    # Extract the dividend and remainder of the current number
    dividend = p // n
    remaining = p % n

    # If the error variable is ON
    if err == 1:
        # Add the corresponding character to the solution
        sol += c[remaining-2]
        # Restart the error variable
        err = 0
    # Otherwise, add the corresponding character
    else:
        sol += c[remaining-1]
    
    # If the remainder is 0, turn ON the error variable
    if remaining == 0:
        err = 1

    # If there are no pending characters
    if dividend == 0:
        # Print the solution and exit the code
        print(sol)
        exit()
    # Otherwise, change the current number and go back
    # to the beginning of the loop
    else:
        p = dividend
