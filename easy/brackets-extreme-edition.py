expression = input()
brack = ")]}"
chain = []
# Result is true until a flaw is found
valid = "true"

for i in expression:
    # Check if an opening bracket appears and if so, insert the
    # corresponding closing one into the first position of the list
    if i == "(":
        chain.insert(0,")")
    elif i == "[":
        chain.insert(0,"]")
    elif i == "{":
        chain.insert(0,"}")

    # Check if the closing character encountered is the next one that
    # should appear and if so, remove it from the list. If not, or the
    # first closing one appears before the first opening one, the result
    # is false
    if i in brack and len(chain) > 0:
        if i == chain[0]:
            del chain[0]
        else:
            valid = "false"
            break

# Check if any closing brackets are still pending or if the original
# expression is only one character long
if len(chain) > 0 or len(expression) == 1:
    valid = "false"

print(valid)
