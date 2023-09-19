print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?\n"))
tip = float(input("what percentage tip would you like to give? 10, 12, o 15?\n"))
people = int(input("how many people to split the bill?\n"))

split = round(((bill * tip /100)+ bill) / people,2)
print(f"Each person should pay: {split}")