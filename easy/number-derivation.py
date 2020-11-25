# Is n a prime number?
def prime(n):
    # If it is 0 or 1, it is not
    if n < 2:
        return False
    # Else if it is 2, it is
    elif n == 2:
        return True
    # If it is another even number, it is not
    elif n % 2 == 0:
        return False
    
    # If no result has been returned, it is an odd number greater than 3
    # Look through all possible divisors between 3 and the suare root of n
    for i in range(3,int(n**0.5)+1,2):
        # If any of them is a divisor, n is not a prime
        if n % i == 0:
            return False
    
    # If no divisor has been found, n is a prime
    return True

# What is the derivative of n?
def derive(n):

    # First divisor to be chedcked is n - 1
    i = n - 1

    # If n is a prime, its derivative is 1
    if prime(n):
        return 1
    # Otherwise
    else:

        # Loops until a return is reached
        while True:
            # If i is a divisor of n, derive the product of
            # the division and i
            if n % i == 0:
                return n//i*derive(i) + derive(n//i)*i
            # Otherwise, check the next possible divisor
            else:
                i -= 1

# Number to be derived
n = int(input())

# Print the solution
print(derive(n))
