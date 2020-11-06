n = int(input())
# Binary code list
bin_list = []
# Ascii code list
asc_list = []

# Read the binary and ascii values and add them to the corresponding lists
for i in range(n):
    b, c = input().split()
    c = int(c)
    bin_list.append(b)
    asc_list.append(c)

# String to be decoded
s = input()
# Count of substrings in string
i = 0
# Solution if no error
sol = ""
# Index for the case where the decoder fails
fail_index = 0

# Look through the string
while i < len(s):
    # For each search, restart the number of fails
    fails = 0
    # Look through every bin string
    for j,bin in enumerate(bin_list):
        l = len(bin)
        # If the current substring of s is equal to the current bin
        if s[i:i+l] == bin:
            # Add the substring to the solution
            sol += chr(asc_list[j])
            # Update the string counter to start at a new index
            i += l
            # Jump to the next bin, since this one has been matched
            break
        # If it is not equal
        else:
            # Increase by 1 the number of fails
            fails += 1
            # Store the current index where it fails
            fail_index = i
    # In case it fails for all the bins, exit while loop
    if fails == n:
        sol = "error"
        break

# If the decoder failed at some point, print where it did
if sol == "error":
    print(f"DECODE FAIL AT INDEX {fail_index}")
# If the decoder worked, print the solution
else:
    print(sol)
