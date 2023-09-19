#ceaser cypher
import Day_8_Art

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
'y', 'z']

#mode selection
print (Day_8_Art.logo)


def cypherthis():
    while True:
        modeword = input('write "encode" to encode a message, write "decode" to decode a message\n').lower()
        if modeword == "decode" or modeword == "encode":
            break
    if modeword.lower() == "decode" :
        mode = -1
    elif modeword.lower() == "encode":
        mode = 1
    else :
        print("invalid")
    #data input
    message = input(f"Write the message you want to {modeword}\n")
    shift = int(input("type in numbers the amount of shift you want\n")) * mode
    while True:
        cypher =""
        index=0
        #main loop
        for _ in message : 
            if letters.count(_) == 0:
                cypher += _
            else : 
                index = (letters.index(_)+shift )% 26    #for overlapping the list.
                cypher += letters[index] 
        return cypher
        

while True:
    print(cypherthis())
    if input("Do you want to play again?").lower() != "yes" : 
        break

    