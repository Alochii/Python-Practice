Random_word = "great"
Random_guess =""
AllowedAttempts = 3
CurrentAttempt= 0
while True:
    Random_guess=input("take a guess!")
    CurrentAttempt += 1
    if Random_guess == Random_word:
        print("YOU DID IT!")
        break
    elif CurrentAttempt >= AllowedAttempts : 
        print("you failed my bro.")
        break
    else :
        continue
