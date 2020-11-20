import math

# Number of rounds
rounds = int(input())
# Initial cash
cash = int(input())

# Look through the rounds
for i in range(rounds):
    # Store the play in a list
    play = input().split()
    # Store the ball position in result and the action
    result = play[0]
    action = play[1]
    
    # The bet is always the rounded up of a quarter of the cash
    bet = math.ceil(cash/4)
    # The cash is reduced by the bet amount
    cash -= bet

    # If the bet is on a single number
    if action == "PLAIN":
        # And the number is the same as the one he bet
        if result == play[2]:
            # He gets back his bet and 35 times it
            cash += bet*36
    # If the bet is on even numbers
    elif action == "EVEN":
        # Adn the number is not 0, but even
        if result != "0" and int(result)%2 == 0:
            # He gets back his bet and one more
            cash += bet*2
    # If the bet is on odd numbers
    else:
        # And the number is odd
        if int(result)%2 != 0:
            # He gets back his bet and one more
            cash += bet*2

# Print the solution
print(cash)
