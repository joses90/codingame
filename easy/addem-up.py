# Number of cards
n = int(input())
# Initialise list of cards
cards = []
# Initialise total cost
cost = 0

# Input every card value and insert it into the list
for i in input().split():
    cards.append(int(i))

# While there is more than one remaining card
while len(cards) > 1:
    # Sort the list of cards in ascending order
    cards = sorted(cards)
    # Add the first two cards together
    cards[0] += cards[1]
    # That new value is the cost of this transaction
    cost += cards[0]
    # Remove the used second card value
    del cards[1]

# Pront the total cost
print(cost)
