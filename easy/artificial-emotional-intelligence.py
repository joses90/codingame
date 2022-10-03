# Name of user
name = input()

# List of adjectives, vowels and consonants
adjList = "Adaptable Adventurous Affectionate Courageous Creative Dependable Determined Diplomatic Giving Gregarious Hardworking Helpful Hilarious Honest Non-judgmental Observant Passionate Sensible Sensitive Sincere".lower().split()
goodList = ["love","forgiveness","friendship","inspiration","epic transformations","wins"]
badList = ["crime","disappointment","disasters","illness","injury","investment loss"]
vowList = [*"aeiouy"]
consList = [*"bcdfghjklmnpqrstvwxz"]

# Initialise lists for vowels and consonants to be used
vow=[]
cons=[]

# For each character in the name
for lett in name.lower():
    # If it is a letter
    if lett.isalpha():
        # If it is a vowel and the the first two vowels in the name have not been registered
        if lett in "aeiouy" and len(vow) < 2:
            # Add the current vowel to the list to be used
            vow.append(lett)
        # If it is a consonante and the the first three unique consonants in the name have not been registered
        elif lett not in "aeiouy" and lett not in cons and len(cons) < 3:
            # Add the current consonant to the list to be used
            cons.append(lett)

# If there were not two vowels and three different consonants in the name
if len(vow)<2 or len(cons)<3:
    print(f"Hello {name}.")
else:
    # Obtain the index of the consonants in conList and obtain the corresponding adjectives
    adj1=adjList[consList.index(cons[0])]
    adj2=adjList[consList.index(cons[1])]
    adj3=adjList[consList.index(cons[2])]

    # Obtain the index of the vowels in vowList and obtain the corresponding good and bad phrases
    good=goodList[vowList.index(vow[0])]
    bad=badList[vowList.index(vow[1])]

    # Print the result
    print(f"It's so nice to meet you, my dear {adj1} {name}.")
    print(f"I sense you are both {adj2} and {adj3}.")
    print(f"May our future together have much more {good} than {bad}.")
