# black jack
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#initialise lists with two cards in them
### get stuck when pc has higher than 16 and i just press continue.
pc = [random.choice(cards),random.choice(cards)]
me = [random.choice(cards),random.choice(cards)]

print(pc, me)


def addcard(list):
    #adds card to a player
    list.append(random.choice(cards))

def checksum(list):
    #checks the total score of a player
    sum = 0
    for _ in list :
        sum += _
    return sum
def checkwin(pc,me,skip):
    if (checksum(pc) == 21 and checksum(me) == 21) or (checksum(pc) > 21 and checksum(me) > 21):
        return 3
    elif checksum(pc) == 21 or checksum(me) > 21 or skip:
        return 2
    elif checksum(me) == 21 or checksum(pc) > 21:
        return 1
    elif skip : 
        if checksum(me) > checksum(pc) : 
            return 1
        elif checksum(me) < checksum(pc) :
            return 2
        else :
            return 3
    else : 
        return 0
    
# 0 is game running, 1 is i won, 2 is pc won, 3 is a tie.
condition = 0
skip = False
choice = ""
while True : 
    print(f"The PC has {pc} or {checksum(pc)} points")
    print(f"i have {me} or {checksum(me)} points")
    print("debug:" ,skip," ",condition," ",choice)
    condition = checkwin(pc,me,skip)
    if condition != 0:
        break
    choice = input("type 1 to add a card, or enter to continue")
    if choice == "1":
        addcard(me)

    if checksum(pc) < 17 :
        addcard(pc)

    skip = False
    if checksum(pc) >= 17 and choice != "1":
        skip = True
        print("skip")
endgame = ["game","You won","The PC won","Its a tie"]
print(endgame[condition])
