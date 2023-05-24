#advanced rock paper scissors.
import random
#starting info
player1 = "Alochii"
player2 = "Megumi"
# winning game messages
winmessage = [
[f"{player2} was just holding a knife, giving you ample time to shoot them",f"{player2}'s muscles are fortunately NOT bullet proof"],
[f"{player2} threw a smokebomb but just..stood in place for some reason. you stabbed through the smoke screen..",f"{player2} planted a bomb!! luckily you were armed with your trustworth bomb-defusal knife."],
[f"{player2} was on steroids, luckily you managed an escape with your smoke bomb. You get to live another day.",f"{player2} pulled out a gun! yet somehow missed every shot through your smoke screen. StormTrooper aim"],
[f"{player2} threw a bomb at you but luckily you were swift enough to throw it back at them",f"{player2} saw how jacked up you are. They got so scared they decided to drop the knife and flee."],
[f"{player2} pulled out a gun.... you know what they say, never bring a gun to a bomb fight.",f"{player2} threw a smokescreen!! .. so you just threw a bomb inside it. they instantly pulvarized. J robert openheimer would be proud"]
]
# losing game messages
losemessage = [
[f"{player2} threw a smoke screen, you empty your clip but manage to miss every shot...","Your gun got jammed. By the time you unjam it, you realise there's a hissing underneath you. Kaboom."],
[f"you brought a knife. {player2} brought a gun. And the rest is history.",f"{player2} has been hitting the gym lately... you fumble your knife but by the time you get a grip on it.. its too late."],
[f"{player2} stabbed you. Did you really think a smokebomb would save you?","you used a smokescreen against a bomb.. a BOMB. Natural selection if you ask me"],
[f"no amount of muscle can hold back a gun. {player2} shoots you",f"{player2} threw a smoke bomb and managed to escape you"],
[f"{player2} used a knife to defuse your bomb. They truly are the best BDMEM in the world.",f"{player2} was quick enough to catch your bomb and throw it at you...yikes."]
]
#0 gun / 1 knife / 2 smokescreen / 3 steroids / 4 bomb
#first two are the choices where your item wins, other two are where the item loses.
indexes = [[[1,3],[2,4]],[[2,4],[0,3]],[[3,0],[1,4]],[[4,1],[0,2]],[[0,2],[1,3]]]

#the game loops here
while True:
    choices = ["gun","knife","smokescreen","steroids","bomb"]
    indexp1 = int(input("Choose what you want to play as :\n1 for gun, 2 for knife, 3 for smoke screen, 4 for steroids, 5 for bomb\n"))-1
    player1choice = choices[indexp1]
    indexp2 = random.randint(0,4)
    print("player 2 chose",choices[indexp2])

    # tied game message
    tiemessage = f"you both used the {player1choice}"

    ''' testing
    for _ in range(0,5):
        for __ in range(0,5):
            indexp1 = _
            indexp2 = __
            print(f"player 1 choice is : {choices[_]}", f", player 2 choice is : {choices[__]}")
    '''
    
    if (indexes[indexp1][0].count(indexp2)):
        print(winmessage[indexp1][indexes[indexp1][0].index(indexp2)])
        print("You win!")
    elif (indexes[indexp1][1].count(indexp2)):
        print(losemessage[indexp1][indexes[indexp1][1].index(indexp2)])
        print("You lose :(")
    else :
        print(tiemessage)
        print("its a tie.")
    input("press enter to play again!")