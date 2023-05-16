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
    
condition = 0
skip = False
choice = ""
pc = [2,10,8]
me = [7,10,5]
while True : 
    print(f"The PC has {pc} or {checksum(pc)} points")
    print(f"i have {me} or {checksum(me)} points")
    print("debug:" ,skip," ",condition," ",choice)
    condition = checkwin(pc,me,skip)
    if condition != 0:
        print("i tried here", condition)
        break
    else : 
        print("condition ",condition)