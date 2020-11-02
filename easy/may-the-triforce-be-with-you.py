# Size of triangles and character to be used
n = int(input())
c = "*"

for i in range(2*n):
    # For first line, include the dot
    if i == 0:
        print("." + " "*2*(n-1)+c)
    # For the first triangle, excluding the top row
    elif i < n:
        print(" "*(2*n-i-1) + c*(2*i+1))
    # For the two bottom triangles
    else:
        j = i - n
        star = c*(2*j+1)
        print(" "*(n-1-j) + star + " "*(2*n-1-2*j) + star)
