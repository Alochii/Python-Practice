import random

#seeds = random.seed()
#print(random.randint(1,6))
#print(random.random())
#coin flip program
'''
check = random.randint(1,2)
if check == 1 :
    print("heads")
elif check == 2 : 
    print("tails")
'''
'''
names = "Alex, Sam, Clover, Buttercups"
nameslist = names.split(", ")
choice = random.randint(0,len(nameslist)-1)
print(f"{nameslist[choice]} will be paying the bill today")
# you can also just use random.choice(names) 
# which will choose a random item from the list
'''

#x marks the treasure
print("where do you want to put thee treasure?")
grid = [["▣","▣","▣"],["▣","▣","▣"],["▣","▣","▣"]]
print(grid[0])
print(grid[1])
print(grid[2])
location = input()
grid[int(location[0])][int(location[1])] = "x"
print(grid[0])
print(grid[1])
print(grid[2])