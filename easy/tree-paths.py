# Nodes in the tree (not used)
n = int(input())
# Index of target node
v = int(input())
# Number of nodes with children
m = int(input())
# Initialise solution
sol = []
# Initialise list of children for each parent
parent = {}

# Look trhough parent nodes and add their children as values
for i in range(m):
    p, l, r = [int(j) for j in input().split()]
    parent[p] = [l,r]
    # Store the node that is the root one
    if i == 0:
        root = p

# If the node is the root one, print "Root"
if root == v:
    print("Root")
# If it is another node
else:
    # Look until the node is the root
    while v != root:
        # Look through the list of parents to look for the child
        # The tree will be searched from bottom to top
        for key in parent:
            # If the child is the left one, add "Left" to the
            # solution and update the current node
            if parent[key][0] == v:
                sol.append("Left")
                v = key
            # Similar to the right one
            elif parent[key][1] == v:
                sol.append("Right")
                v = key

    # Invert the list, since we need the solution from top to bottom
    sol = sol[::-1]
    # Print the solution
    print(*sol)
