#Create a band name generator!
print("___________________________________________________\n")
print("Hello there! Welcome to the Band Name generator 2.4")
print("To generate a band name, all you need to do is answer some questions")
city = input("What city were you born in?\n")
pet = input("what's the name of your pet? you can answer \"no\" if you didnt have any\n")

if pet == "no":
    print(f"your band name is abandoned {city}")
else :
    print(f"your band name is {city} {pet}")
print("___________________________________________________")

#day 1 finished in 50 minutes.