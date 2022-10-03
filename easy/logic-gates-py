# Number of input and output signals
n = int(input())
m = int(input())

# Initialise dictionaries to store all inputs and operations needed
inp,sol = {},{}

# Store input and operations signals
for i in range(n):
    input_name, input_signal = input().split()
    inp[input_name] = input_signal
for i in range(m):
    output_name, _type, input_name_1, input_name_2 = input().split()
    sol[output_name] = [_type, input_name_1, input_name_2]

# Look through outputs needed
for i in range(m):
    # Store in different variables: the output name, the gate applied and the two input signals
    outp,gate,string_1,string_2 =[*sol][i],sol[[*sol][i]][0],inp[sol[[*sol][i]][1]],inp[sol[[*sol][i]][2]]
    # Initalise output
    res=outp+' '

    # Look through characters in input signals
    for j in range(len(string_1)):
        c1,c2 = string_1[j],string_2[j]
        # Check the gate operation and j character in both input signals to obtain the
        # j character for the input
        # Repeat the equivalent operation for the other gates
        if gate == 'AND':
            if(c1=='-' and c2=='-'):
                res+='-'
            else:
                res+='_'
        elif gate == 'OR':
            if(c1=='-' or c2=='-'):
                res+='-'
            else:
                res+='_'
        elif gate == 'XOR':
            if((c1=='-' or c2=='-') and c1!=c2):
                res+='-'
            else:
                res+='_'
        elif gate == 'NAND':
            if(c1=='-' and c2=='-'):
                res+='_'
            else:
                res+='-'
        elif gate == 'NOR':
            if(c1=='-' or c2=='-'):
                res+='_'
            else:
                res+='-'
        elif gate == 'NXOR':
            if((c1=='-' or c2=='-') and c1!=c2):
                res+='_'
            else:
                res+='-'

    # Print the result for this output
    print(res)
