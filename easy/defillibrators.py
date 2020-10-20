import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

min_dist = math.inf
lon = input()
lat = input()
lon = float(lon.replace(',', '.'))
lat = float(lat.replace(',', '.'))
n = int(input())
for i in range(n):
    defib = input()
    num_def, name_def, add_def, phone_def, lon_def, lat_def = defib.split(";")
    lon_def = float(lon_def.replace(',', '.'))
    lat_def = float(lat_def.replace(',', '.'))
    dis_x = (lon_def - lon)*math.cos((lat + lat_def)/2)
    dis_y = (lat_def - lat)
    dis = math.sqrt(dis_x**2 + dis_y**2)*6371
    if dis < min_dist:
        min_dist = dis
        sol = name_def

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(sol)
