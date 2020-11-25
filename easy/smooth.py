# Number of games/weeks
n = int(input())
# For each week
for i in range(n):
    # Quantity of food available
    f = int(input())
    # Loop until victory or defeat
    while True:
        # If the amount of fruit left is one, the game is won
        if f == 1:
            print("VICTORY")
            break
        # If the amount of fruit left is divisible by 5,
        # divide it by 5
        elif f%5 == 0:
            f = f//5
        # Same for the 3 and 2
        elif f%3 == 0:
            f = f//3
        elif f%2 == 0:
            f = f//2
        # Otherwise, the game is lost
        else:
            print("DEFEAT")
            break
