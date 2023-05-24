import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

lets = int(input("how many letters if your password?"))
syms = int(input("how many symbols does it have?"))
nums = int(input("how many numbers does it have?"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#easy : 
pass1 = ""
for _ in range (1, lets+1):
    pass1 += str(random.choice(letters))
for _ in range (1, syms+1):
    pass1 += str(random.choice(symbols))
for _ in range (1, nums+1):
    pass1+= str(random.choice(numbers))

pass1 = list(pass1.strip(" "))
random.shuffle(pass1)
password = ""
for _ in pass1:
    password += _
print(password)

#hard : 
'''
iterations = lets + nums + syms 
password =""
while iterations > 0 : 
    pickrandom = random.randint(1,3)
    if pickrandom == 1 and lets > 0 : 
        password += str(random.choice(letters))
        lets -= 1
    elif pickrandom == 2 and syms > 0 : 
        password+= str(random.choice(symbols))
        syms -= 1
    elif pickrandom == 3 and nums > 0 : 
        password+= str(random.choice(numbers))
        nums -= 1
    else : 
        iterations += 1
    iterations -= 1
print(password)
# you can just use the shuffle function XD fuck me.
'''