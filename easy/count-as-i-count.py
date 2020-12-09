# Current score
n = int(input())
# Remaining score to reach 50
rem = 50 - n
# Initialise count of possible permutations
count = 0

# List of possible scores per throw
lis = ["P1","P2","P3","P4","P5","P6","P7","P8","P9","P10","P11","P12","0","2","3","4","5","6","7","8","9","10","11","12"]

# Look through the 1st round
for i in lis:
    # Extract the score from the throw
    if "P" in i:
        sol = int(i[1:])
    else:
        sol = int(i)
    
    # If the score is equal to the remaining, include this permutation
    if sol == rem:
        count += 1
        #print(i)
    # If it is a 0, ignore the following rounds
    elif i == "0":
        pass
    # If it less than the remaining, go to the next round
    elif sol < rem:
        # Look through the 2nd round and do a similar analysis
        for j in lis:
            if "P" in i:
                sol = int(i[1:])
            else:
                sol = int(i)
            if "P" in j:
                sol += int(j[1:])
            else:
                sol += int(j)            

            if sol == rem:
                count += 1
            elif j == "0":
                pass
            elif sol < rem:
                # Look through the 3rd round and do a similar analysis
                for k in lis:
                    if "P" in i:
                        sol = int(i[1:])
                    else:
                        sol = int(i)
                    if "P" in j:
                        sol += int(j[1:])
                    else:
                        sol += int(j)
                    if "P" in k:
                        sol += int(k[1:])
                    else:
                        sol += int(k)             

                    if sol == rem:
                        count += 1
                    elif k == "0":
                        pass
                    elif sol < rem:
                        # Look through the 4th round and do a similar analysis         
                        for l in lis:
                            if "P" in i:
                                sol = int(i[1:])
                            else:
                                sol = int(i)
                            if "P" in j:
                                sol += int(j[1:])
                            else:
                                sol += int(j)
                            if "P" in k:
                                sol += int(k[1:])
                            else:
                                sol += int(k)
                            if "P" in l:
                                sol += int(l[1:])
                            else:
                                sol += int(l)       

                            if sol == rem:
                                count += 1

# Print the count of possible permutations
print(count)
