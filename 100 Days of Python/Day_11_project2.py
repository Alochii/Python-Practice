# black jack attempt 2
import random 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
print("""
__________                        __          ____.              __    
\______   \_______   ____ _____  |  | __     |    |____    ____ |  | __
 |    |  _/\_  __ \_/ __ \\\__  \ |  |/ /     |    \__  \ _/ ___\|  |/ /
 |    |   \ |  | \/\  ___/ / __ \|    <  /\__|    |/ __ \\  \___|    < 
 |______  / |__|    \___  >____  /__|_ \ \________(____  /\___  >__|_ \\
        \/              \/     \/     \/               \/     \/     \/
""")
print("you're in a russian prison and you have 100 bucks to your name")
print("your only chance to escape is to collect a thousand bucks to bribe the guards")
messages = {
    1 : "you won. Blackjack",
    2 : "overdrawn. you lost",
    3 : "Its a tie.",
    4 : "you win!",
    5 : "you got blackjacked",
    6 : "you win. the AI overdrew",
    7 : "you lose. good day sir",
}


def drawcard(player):
    #adds a card to selected player's list
    player.append(random.choice(cards))

def cardscore(player):
    #calculates total score of selected player
    score = 0
    for _ in player:
        score += _
    #this is to count aces as 1 incase the score is more than 21
    acecount = player.count(11)
    while score > 21  and acecount != 0: 
        score -= 10
        acecount -= 1
    return score

def wincondition(player,AI,input):
    #21?
        # other 21? Tie X
        # other not 21? win X
    # > 21?
        # other > 21? Tie X
        # other not > 21? lose X
    # < 21?
        # if input = 1 : continue
        # else : 
            # AI > 17?
                #player > AI ? #win
                #player < AI?
                    #AI = 21? lose
                    #AI > 21? win 
                    #AI < 21? lose
            # AI < 17?
                #continue
    if cardscore(player) == 21:
        if cardscore(AI) == 21 :
            #print("tie")
            return 3
        else : 
            #print("you won. Blackjack")
            return 1
    elif cardscore(player) > 21 :
        if cardscore(AI) > 21 : 
            #print("its a tie")
            return 3
        else :
            #print("overdrawn. you lost")
            return 2
    elif cardscore (player) < 21 : 
        if input == "1" : 
            return 0
        elif input == "0" : 
            if cardscore (AI) >= 17 : 
                if cardscore(player) > cardscore(AI):
                    #print("you win!")
                    print(cardscore(player),cardscore(AI))
                    return 4
                elif cardscore(player)<cardscore(AI):
                    if cardscore(AI) == 21 :
                        #print("you lost, blackjack")
                        return 5
                    elif cardscore(AI) > 21 :
                        #print("you win. the AI overdrew")
                        return 6
                    else : 
                        #print("you lose. good day sir")
                        print(cardscore(player),cardscore(AI))
                    return 7
                else : 
                    #print("tie")
                    return 3
            elif cardscore (AI) < 17 :
                print("the AI drew a card!")
                return 0

runtime = "y"
money = 100
while runtime == "y":   
    #initialise lists with two cards in them
    player = []
    AI = []        
    for _ in range(2):
        drawcard(player)
        drawcard(AI)

# check win condition, if not (ingame) then break out and print win message
# input = 0
# input here
# if input 1 : draw 
    play = "1"
    print(f"Money : {money}")
    while True:
        bet = int(input("how much will you bet?"))
        if bet <= money : 
            break
        else : 
            print("you can't bet more money than you have!") 

    while True :
        print("Player hand : ",player,", score :",cardscore(player))
        print("AI's hand :   ",AI,", score : ",cardscore(AI))
        condition = wincondition(player,AI,play)
        
        if condition != 0:
            break
        play = "0"
        play = input("draw a new card? type 1 to add new card, or 0 to pass\n")
        if play == "1" : 
            drawcard(player)
        if cardscore(AI) < 17 :
            drawcard(AI)

    print(messages[condition])
    if condition == 1 or condition == 4 or condition == 6:
        money += bet
    elif condition == 2 or condition == 5 or condition == 7:
        money -= bet
    if money >= 1000 : 
        print("you manage to get the money with skillful manoeuvre and a LOT of blind luck")
        print("you bribe the guards and escape prison")
        break
    elif money <= 0 :
        print("you're now stuck in a russian prison. forever.")
        break
    else : 
        runtime = input("want to play again? y to play, n to stop playing")
