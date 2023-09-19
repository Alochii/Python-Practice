#some conditional practice and stuff. 
#BMI CALCULATOR
'''
weight = int(input("what is your weight in kilograms?\n"))
height = float(input("what is your height in meters?\n"))
BMI = weight / (height*height)

if (BMI < 35):
    if (BMI < 30):
        if (BMI < 25):
            if (BMI < 18.5):
                print(f"your BMI is {BMI}, thus you are underweight")
            else:
                print(f"your BMI is {BMI}, thus you have normal weight")
        else:
            print(f"your BMI is {BMI}, thus you are overwight")
    else : 
        print(f"your BMI is {BMI}, thus you are obese")
else : 
    print(f"your BMI is {BMI}, thus you are clinically obese")

'''

#is it a leap year?
'''
year = float(2028)
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("leap year")
        else : 
            print("not leap year")
    else : 
        print("leap year")
else : 
    print("not leap year")
'''

#pizza shop
'''
print("Welcome to Python Pizza Deliveries!\n")

size = input("What size pizza do you want? S, M or L?\n").upper()
print(size)
add_pepperoni = input("do you want pepperoni? Y, N\n").upper()
extra_cheese = input("Do you want extra cheese? Y, N\n").upper()

total = 0
if size == "L" : 
    total += 25
elif size == "M" : 
    total += 20
elif size == "S" :
    total += 15

if add_pepperoni == "Y":
    if size == ("L" or "M") :
        total += 3
    elif size == "S" : 
        total += 2

if extra_cheese == "Y" :
    total += 1

print(f"your total comes out to ${total}. thank you shopping with mama and mittie shop")
'''

#the love calculator
'''
print("Welcome to the love calculator!")
#name1 = input ("enter the soon to be husband's name\n")
name1 = "Mahfoud Ali"
#name2 = input ("enter the soon to be wife's name\n")
name2 = "Megumi Charkaboti"
scoretrue = 0
scorelove = 0
for _ in "bunnybaby":
    scoretrue += name1.lower().count(_)
    scoretrue += name2.lower().count(_)
for _ in "mitten":
    scorelove += name1.lower().count(_)
    scorelove += name2.lower().count(_)

score = scoretrue*10 +scorelove
print(score)

if score < 10 or score > 90 :
    print(f"your score is {score}, you go together like coke and mentos")

elif score > 40 and score < 50 : 
    print(f"your score is {score}, you two go alright together")
else : 
    print(f"your score was {score}")
'''