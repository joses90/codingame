# Available alphabet
_input = input().replace(" ","")
# newible states
states = input().split()
# Number of different transitions
number_of_transitions = int(input())
# Initialise the list of transitions
transi = []

# Store the transitions available
for i in range(number_of_transitions):
    transi.append(input().replace(" ",""))

# Start state and list of allowed end states
start_state = input()
end_states = input().split()
# Number of words to check
number_of_words = int(input())

# Look through the list of words
for i in range(number_of_words):
    # Store the word
    word = input()
    # The start date after every transition is initialised
    start = start_state

    # Look through the letters in the word
    for t,let in enumerate(word):
        # If the letter is in the alphabet
        if let in _input:
            # If the combination with start state "start" and letter "let" exists
            try:
                # Extract the correct transition
                new = [j for j in transi if j[0] == start and j[1] == let][0]
                # The new start state is the end state of the found transition
                start = new[2]
            # Otherwise, the solution is false. Go to the next word
            except IndexError:
                print("false")
                break

            # If we are already in the last letter of the word               
            if t == len(word) - 1:
                # And the current state is in the list of end states,
                # the solution is true
                if start in end_states:
                    print("true")
                # Otherwise, the solution is false
                else:
                    print("false")
        # Otherwise, the solution is false. Go to the next word
        else:
            print("false")
            break
