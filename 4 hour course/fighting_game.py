from Pokemons import pokemon
# name, level, type, health, attack, defence.
enemy1= pokemon("charmander", 15, "fire", 150,50, 25)
your_pk = pokemon("balbasaur", 20, "grass", 200, 20, 40)
enemy2 = pokemon("squirtel", 12, "water", 170, 40, 30)

YourHealth = your_pk.health
EnemyHealth = enemy1.health
print(YourHealth)
print(EnemyHealth)
# health - ( (defence - attack but not below 0))
while YourHealth > 0 and EnemyHealth > 0 : 
    print(enemy1.attack - your_pk.defence)
    if enemy1.attack - your_pk.defence  > 0 : 
        YourHealth -= (enemy1.attack - your_pk.defence)
    print("your health : ", YourHealth)

    print(your_pk.attack - enemy1.defence)
    if your_pk.attack - enemy1.defence  > 0 : 
        EnemyHealth -= (your_pk.attack - enemy1.defence)
    print("enemy health : ", EnemyHealth)
    input()

if YourHealth > EnemyHealth : 
    print ("you won!")
elif EnemyHealth > YourHealth : 
    print("get bent idiot. go back to the grass area where you belong")
else : 
    print("its a tie!")