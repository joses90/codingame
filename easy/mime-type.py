# Number of MIME types in association table
n = int(input())
# Number of files to analyse
q = int(input())
# Initialise dictionary to store extensions and their MIME type
dic = {}

# Look through every MIME type
for i in range(n):
    # Extract the extension and type and store its uppercase value in the dictionary
    ext, mt = input().split()
    dic[ext.upper()] = mt

# Look through every file to be analysed
for i in range(q):
    # Store the file name
    fname = input()
    
    # If there is a dot in the name
    if '.' in fname:
        # Extract the text entension after the last dot and uppercase it
        exten = fname.split('.')[-1].upper()
        # If it is in the association table, print the MIME type
        if exten in dic:
            print(dic[exten])
        # Otherwise, the MIME type is unknown
        else:
            print("UNKNOWN")
    # Otherwise, the MIME type is unknown
    else:
        print("UNKNOWN")
