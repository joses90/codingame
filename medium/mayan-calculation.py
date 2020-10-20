import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l, h = [int(i) for i in input().split()]
num_all = []
num_1 = []
num_2 = []
for i in range(h):
    numeral = input()
    num_all.append(numeral) # One line per list element
s1 = int(input())
for i in range(s1):
    num_1line = input()
    num_1.append(num_1line)
s2 = int(input())
for i in range(s2):
    num_2line = input()
    num_2.append(num_2line)
operation = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# Convert the two numbers to arab numbers
nums = list(range(20))
num_1_base20 = [nums.copy() for i in range(int(s1/h))]
# print("Numbers", num_1_base20, file=sys.stderr, flush=True)
num_2_base20 = [nums.copy() for i in range(int(s2/h))]
for t in range(int(s1/h)):
    for i in range(h):
        for k in range(20):
            if num_all[i][l*k:l*(k+1)] != num_1[i+t*h][:] and k in num_1_base20[t]:
                num_1_base20[t].remove(k)
                # print("c =",num_all[i][l*k:l*(k+1)], num_1[i+t*h][:], "\n", file=sys.stderr, flush=True)
                # print("Remove =",k, "\n", file=sys.stderr, flush=True)
                # print("l =",num_1_base20, "\n", file=sys.stderr, flush=True)

for t in range(int(s2/h)):
    for i in range(h):
        for k in range(20):
            if num_all[i][l*k:l*(k+1)] != num_2[i+t*h][:] and k in num_2_base20[t]:
                num_2_base20[t].remove(k)
                # print("c =",num_all[i][l*k:l*(k+1)], num_2[i+t*h][:], "\n", file=sys.stderr, flush=True)
                # print("Remove =",k, "\n", file=sys.stderr, flush=True)
                # print("l =",num_2_base20, "\n", file=sys.stderr, flush=True)
# print("Numbers arabic =", num_1_base20, num_2_base20, file=sys.stderr, flush=True)

# Simplify the numbers to easier lists
num_1_simp = []
num_2_simp = []
for i in num_1_base20:
    num_1_simp.append(i[0])
for i in num_2_base20:
    num_2_simp.append(i[0])
# print("Number 1 in base20: ",num_1_simp, file=sys.stderr, flush=True)
# print("Number 2 in base20: ", num_2_simp, file=sys.stderr, flush=True)

# Convert base20 numbers into normal base10 numbers
num_1_base10 = 0
l_1 = len(num_1_simp)
for i in range(l_1):
    num_1_base10 = num_1_base10 + num_1_simp[i]*(20**(l_1-i-1))
# print("Number 1 in base10: ", num_1_base10, file=sys.stderr, flush=True)

num_2_base10 = 0
l_2 = len(num_2_simp)
for i in range(l_2):
    num_2_base10 = num_2_base10 + num_2_simp[i]*(20**(l_2-i-1))
# print("Number 2 in base10: ", num_2_base10, file=sys.stderr, flush=True)

# Operate them and store the result in sol_arab
# If operator is not valid, a string is returned
if operation in ("*","/","+","-"):
    sol_arab = eval(str(num_1_base10) + operation + str(num_2_base10))
    sol_arab = int(sol_arab)
    sol = ""
    sol20 = []
    rem = 999
    # Show operation done
    print(num_1_base10, operation, num_2_base10,"=", sol_arab, file=sys.stderr, flush=True)
    # Convert the solution from normal base10 to base20
    # and store it in sol20
    while sol_arab > 20:
        rem = sol_arab % 20
        # print("Remaining = ", rem, file=sys.stderr, flush=True)
        sol_arab = int(sol_arab/20)
        # print("Sol_arab = ", sol_arab, file=sys.stderr, flush=True)
        sol20.append(rem)
    sol20.append(sol_arab)
    sol20.reverse()
    #print("Base20 = ", sol20, file=sys.stderr, flush=True)

    # Print in mayan numbers the base20 solution (one below the other as requested)
    for k in sol20:
        for i in range(h):
            sol = sol + num_all[i][l*k:l*(k+1)] + "\n"
else:
    sol = "Operator provided not valid, it should be +, -, * or /"

print(sol)
# print(sol20,num_1_base20, num_2_base20, sol_arab,"\n", sol)
