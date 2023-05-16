#numbers guessing game
import random

def checkwin(guess,solution,tries):
    
    if guess > solution : 
        if tries == 0:
            return 0
        print("Try to guess lower")
        return 0
    elif guess < solution :
        if tries == 0:
            return 0 
        print("try to guess higher")
        return 0
    else : 
        print("you got it!")
        return 1
def game():
    solution = random.randint(1,100)
    print("welcome to the numbers guessing game!")
    triestext =""
    while triestext != "hard" and triestext != "easy":
        triestext = input('Type "easy" to play in easy difficulty, or "hard" to play in hard difficulty\nYour difficulty : ').lower()
    if triestext == "hard".lower():
        tries = 5
    elif triestext == "easy".lower():
        tries = 10
    while True : 
        if tries == 0:
            print(f"you ran out of attempts. the number you were looking for was {solution}")
            break
        print(f"you have {tries} tries remaining")
        guess = int(input("try to guess the number!\nyour guess : "))
        tries -= 1
        if checkwin(guess,solution,tries) == 1 :
            break
    
game()


