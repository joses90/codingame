# Number of robbers and vaults
r = int(input())
v = int(input())
# List to store the current times of each robber
lis = []
# Counter to check the first r vaults (one per robber)
j = 0
for i in range(v):
    # Number of characters (including numbers) for each combination
    # and numbers in that combination
    c, n = [int(j) for j in input().split()]
    # Possible combination for n different numbers and (c-n) different vowels
    comb = (10**n)*(5**(c-n))
    # Fill the list with the first r vaults
    if j < r:
        lis.append(comb)
        j += 1
    # Check for the rest of the vaults
    else:
        # The current minimum value is the robber that finishes first its current
        # vault and will need to work on the next one, thus updating his/her time.
        mins = min(lis)
        for k,val in enumerate(lis):
            if val == mins:
                lis[k] += comb

# The time to open all vaults is the maximum of the time it takes each robber.
sol = max(lis)
print(sol)
