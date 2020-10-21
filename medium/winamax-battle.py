import sys
import math

cards_1 = []
cards_2 = []
value = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13,"A":14}
n = int(input())  # the number of cards for player 1
for i in range(n):
    cardp_1 = input()  # the n cards of player 1
    cards_1.append(cardp_1)
m = int(input())  # the number of cards for player 2
for i in range(m):
    cardp_2 = input()  # the m cards of player 2
    cards_2.append(cardp_2)
print("Cards Player 1: ", cards_1, file=sys.stderr, flush=True)
print("Cards Player 2: ", cards_2, file=sys.stderr, flush=True)

rounds = 0
run_out = 0

while len(cards_1) > 0 and len(cards_2) > 0:
    rounds += 1
    if value[cards_1[0][0:-1]] > value[cards_2[0][0:-1]]:
        cards_1.extend([cards_1[0], cards_2[0]])
        del cards_1[0], cards_2[0]
    elif value[cards_1[0][0:-1]] < value[cards_2[0][0:-1]]:
        cards_2.extend([cards_1[0], cards_2[0]])
        del cards_1[0], cards_2[0]
    else:
        if len(cards_1) < 5 and len(cards_2) < 5:
            run_out = 1
            break
        elif value[cards_1[4][0:-1]] > value[cards_2[4][0:-1]]:
            cards_1.extend([cards_1[0:5], cards_2[0:5]])
            del cards_1[0:5], cards_2[0:5]
        elif value[cards_1[4][0:-1]] < value[cards_2[4][0:-1]]:
            cards_2.extend([cards_1[0:5], cards_2[0:5]])
            del cards_1[0:5], cards_2[0:5]
        
        # break
    # print("Round", rounds, "Player 1: ", cards_1, len(cards_1), file=sys.stderr, flush=True)
    # print("Round", rounds, "Player 2: ", cards_2, len(cards_2), "\n", file=sys.stderr, flush=True)
    print("Round", rounds, "Player 1: ", cards_1[0:3],cards_1[-4:], len(cards_1), file=sys.stderr, flush=True)
    print("Round", rounds, "Player 2: ", cards_2[0:3],cards_2[-4:], len(cards_2), "\n", file=sys.stderr, flush=True)

if len(cards_1) == 0:
    sol = "2 " + str(rounds)
elif len(cards_2) == 0:
    sol = "1 " + str(rounds)
elif run_out == 1:
    sol = "PAT"
print("Player 1 end: ", cards_1, file=sys.stderr, flush=True)
print("Player 2 end: ", cards_2, file=sys.stderr, flush=True)

print(sol)
