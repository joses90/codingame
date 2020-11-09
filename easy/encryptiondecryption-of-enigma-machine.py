# To be able to import messages before the end
import sys

# Input the message to be applied an n-shift, depending if it needs
# to be ENCODED or DECODED
def caesarf(message,n,oper):
    # Initialise the solution with the "caesared"/"uncaesared" message
    caesar = ""

    # If you want to encode the message
    if oper == "ENCODE":
        # Look through the message
        for i,let in enumerate(message):
            # Obtain the position in the alphabet for each letter in the message
            # using the ascii code (ord(letter) + 65), the shift (n) and the index (i)
            c = ord(let) - 65 + n + i
            # If the position of the alphabet is between 0 and 25, add the letter to the solution
            if c <= 25:
                caesar += chr(c+65)
            # Otherwise, the position is outside the alphabet
            else:
                # Decrease the position by the length of the alphabet until it falls inside,
                # then add the resulting letter to the solution
                while c > 25*2 + 1:
                    c -= 26
                caesar += chr(c-26+65)
    # If you want to decode the message
    elif oper == "DECODE":
        # Similar idea to ENCODE but checking if the position is below 0
        for i,let in enumerate(message):
            c = ord(let) - 65 - n - i
            if c < 0:
                while c < -26:
                    c += 26
                caesar += chr(c+26+65)
            else:
                caesar += chr(c+65)

    # Return the "caesared"/"uncaesared" message
    return caesar

# Apply change to message from alph to rotor
def rotorf(message,alph,rotor):
    #Initialise solution
    rotored = ""
    # Look through the message
    for i, let in enumerate(message):
        # Find the index in alph where the current letter is and add to the solution,
        # the letter that has that position in rotor
        rotored += rotor[alph.index(let)]

    # Return the "rotored"/"unrotored" message
    return rotored

# Alphabet
alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# ENCODED / DECODED
operation = input()
# Shift to be applied for the Caesar shift
pseudo_random_number = int(input())

# Initialise list of rotors
rotors = []
# Add rotors strings to the list
for i in range(3):
    rotors.append(input())
# Message to be encoded/decoded
message = input()

# If the message is to be encoded
if operation == "ENCODE":
    print("Rotors:     ",rotors, file=sys.stderr, flush=True)
    print("Message:     ",message, file=sys.stderr, flush=True)
    # First: "caesar" the message
    caesar = caesarf(message,pseudo_random_number,operation)

    print("Caesar:      ",caesar, file=sys.stderr, flush=True)

    # Second: "rotor" the message
    # Initialise the message to be "rotored"
    messa = caesar
    # Go through every rotor
    for i in range(3):
        # The message messa is searched through alph to return the value
        # in the current rotor
        messa = rotorf(messa,alph,rotors[i])
        print(f"Rotor {i+1}:      {messa}", file=sys.stderr, flush=True)
# If it needs to be decoded
else:
    print("Rotors:     ",rotors, file=sys.stderr, flush=True)
    print("Message:     ",message, file=sys.stderr, flush=True)

    # First: "unrotor" the message
    messa = message
    # Looking through rotors in reverse
    for i in range(2,-1,-1):
        # The message messa is searched through the current rotor to return the value
        # in alph
        messa = rotorf(messa,rotors[i],alph)
        print(f"Rotor {i+1}:      {messa}", file=sys.stderr, flush=True)

    # Second "uncaesar" the message
    messa = caesarf(messa,pseudo_random_number,operation)
    print("Caesar:      ",messa, file=sys.stderr, flush=True)

print("", file=sys.stderr, flush=True)
# The result is printed
print(messa)
