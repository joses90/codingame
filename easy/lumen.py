# Dimensions of square map
n = int(input())
# Base light of candles
l = int(input())
# List to store position of candes in the grid
candles = []
# List to store cells with no candles
no_candles = []

# Look for cell value
for i in range(n):
    for j,cell in enumerate(input().split()):
        # If there is a candle, include that cell into the candles list
        if cell == "C":
            candles.append([i,j])
        # If it is not, add it to the no_candles list
        else:
            no_candles.append([i,j])

# Create a copy of the no_candles list.
# In this new one, if the light reaches a cell, this will be removed from the list
no_light = no_candles[:]

# Look through every cell that has no candle
for cell in no_candles:
    # Look through the list of cells with candles
    for candle in candles:
        # Obtain the distance between the current cell and candle
        x_diff = abs(cell[0] - candle[0])
        y_diff = abs(cell[1] - candle[1])
        # If it is within range of the candle
        if x_diff < l and y_diff < l:
            if cell in no_light:
                # Remove the cell from the no_light list and skip to the next cell
                no_light.remove(cell)
                break

# Output the number of cells with no light
print(len(no_light))
