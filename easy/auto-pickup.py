# Length of the packet
n = int(input())
# Packet to be inspected
packet = input()

# Look through the packet
while True:
    # Extract the instruction (first three bits)
    instruction = packet[:3]
    # Extract the binary representation of the packet length
    pack_len = packet[3:7]
    # Convert that length to base 10
    pack_len_int = int(pack_len,2)
    # Extract the item_id with a length equal to the one obtained above
    item_id = packet[7:7+pack_len_int]

    # If the instrction was "101"
    if instruction == "101":
        # Print the response
        print("001" + pack_len + item_id,end="")

    # Update the packet to ignore the characters already used
    packet = packet[7+pack_len_int:]

    # If the remaing length is less than 7, exit the loop
    if len(packet) < 7:
        break
