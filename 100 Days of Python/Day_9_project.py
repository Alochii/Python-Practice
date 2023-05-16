#blind bidding game

Participants = {}

def addbidder():
    condition = 1
    while condition == 1:
        name = input("name\n")
        bid = int(input("bid\n"))
        Participants[name] = bid
        if input("type no if there are no other bidders, otherwise press enter?\n") == "no":
            condition = 0

def highestbid():
    maxbid = 0
    winner = ""
    for _ in Participants:
        if Participants[_] > maxbid:
            maxbid = Participants[_]
            winner = _
    print(f"the winner is {winner} with a bet of {maxbid}")

    
addbidder()
print(Participants)

highestbid()


