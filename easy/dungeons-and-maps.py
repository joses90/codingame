import math

# Width and height of each map
w, h = [int(i) for i in input().split()]
# Starting row and column. Same for each map
start_row, start_col = [int(i) for i in input().split()]
# Number of maps
n = int(input())

# Initialise map dictionary, one key per map. Each with an empty list
maps = {i:[] for i in range(n)}
# Write every row in a different element for each list for each key
for i in range(n):
    for j in range(h):
        maps[i].append(input())

# Look through each map
for i in range(n):
    # Starting position for each map
    pos = [start_row, start_col]
    # Longitude of the path so far
    lon = 0

    # Loop until a "#", "." or out of map is found
    while True:
        # Store the current position, to be updated after every loop
        cell = maps[i][pos[0]][pos[1]]
        # If the treasure is encountered, update the dictionary value
        # for that map with the longitude
        # TREASURE: Exit the loop to check the next map
        if cell == "T":
            maps[i] = lon + 1
            break
        # If the path is circular and thus, neverending, the path is infinite.
        # TRAP: Exit the loop to check the next map
        elif lon > w*h:
            maps[i] = math.inf
            break
        # If the instruction is going up and that next cell is inside the map,
        # increase the length of the path and update the position
        elif cell == "^" and pos[0]-1 > 0:
            lon += 1
            pos[0] -= 1
        # Similarly for the down, right and left movements
        elif cell == "v" and pos[0]+1 < h:
            lon += 1
            pos[0] += 1
        elif cell == ">" and pos[1]+1 < w:
            lon += 1
            pos[1] += 1
        elif cell == "<" and pos[1]-1 > 0:
            lon += 1
            pos[1] -= 1
        # If the next position is out of the map
        # TRAP: Exit the loop to check the next map
        else:
            maps[i] = math.inf
            break

# If all maps have an infinite solution, output TRAP
if all(path == math.inf for path in maps.values()):
    print("TRAP")
# If at least one of them has a path, output the map that has a shortest map
else:
    mins = min(maps, key=maps.get)
    print(mins)
