# Number of lines
n = int(input())
# Counters for first time Fizz, Buzz and FizzBuzz are encountered
fizz_1 = 0
fizz_2 = 0
buzz_1 = 0
buzz_2 = 0
# First number found
numb = 0

# Look through each line
for i in range(n):
    # Store the value
    num = input()

    # If it is not a number
    if not num.isnumeric():
        # If it is "Fizz"
        if num  == "Fizz":
            # And no "Fizz" or "FizzBuzz" has been found,
            # store the index for that text
            if fizz_1 == 0:
                fizz_1 = i
            # And one "Fizz" or "FizzBuzz" has been found,
            # but not the second one, store the indez
            elif fizz_2 == 0:
                fizz_2 = i
        # Similar for "Buzz"
        elif num == "Buzz":
            if buzz_1 == 0:
                buzz_1 = i
            elif buzz_2 == 0:
                buzz_2 = i
        # Similar for "FizzBuzz"
        elif num == "FizzBuzz":
            if fizz_1 == 0:
                fizz_1 = i
            elif fizz_2 == 0:
                fizz_2 = i
            if buzz_1 == 0:
                buzz_1 = i
            elif buzz_2 == 0:
                buzz_2 = i
    # If it is the first number
    elif num.isnumeric() and numb == 0:
        # Store the number value and its index
        numb = int(num)
        inde = i

# The difference in indices is the solution
fizz = fizz_2-fizz_1
buzz = buzz_2-buzz_1

# If only one instance of "Fizz" and "FizzBuzz" combined is found
if fizz_2 == 0:
    # Update the value of "Fizz" using the number encountered
    fizz = fizz_1 - inde + numb
# If only one instance of "Buzz" and "FizzBuzz" combined is found
if buzz_2 == 0:
    # Update the value of "Buzz" using the number encountered
    buzz = buzz_1 - inde + numb

# Print the solution
print(fizz,buzz)
