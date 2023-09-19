# The quick python basics guide by yours truly Alochii
# how to print
print("hello world")
# variable types
name = "frisky"      # strings
print(name)
num = 64.2               # float and ints
print(num, "\n")
condition = False        # boolean
print(condition)
# casting
print(int(num))          # casting a float into int
# conditional
name2 = "jonathan"
if name2 == "jonathan":     # == for equal to. and != not equal to
    print("welcome ", name2)
else:
    print("you're not the user")
name3 = name + name2    # math operands. + - * / % **
print(name3)
A = 1
B = 2
if A or B == 1:
    print("yes")
# comparison  and while loops
while A <= 5:
    print(A)
    A += 1
# lists
groceries = ["veggies", "match sticks", "batteries"]
print(len(groceries))    # list methods
groceries[1] = "salad"   # list modifying
groceries.append("milky")
print(groceries[3])
print("batteries" in groceries)   # this print True
# for loops
for i in range(5):
    print(i)               # prints 0 to 4
for item in groceries:
    print(item)            # prints items in the list
# exceptions
try:                       # try to run this code
    for i in range(5):
        print(groceries[i])    # items from index 0 to 4. and 4 doesn't exist
except IndexError as error:  # do this if there's an error
    print(error)
else:                      # if no error, run this
    print("no error here")
finally:                   # run this regardless of the outcome at the end
    print("code is done")


# functions
def welcome_msg(user_name, time):
    if time < 2100:
        if time < 1800:
            if time < 1150:
                if time < 500:
                    day_time = "night"
                else:
                    day_time = "morning"
            else:
                day_time = "afternoon"
        else:
            day_time = "evening"
    else:
        day_time = "night time"
    print(f"welcome back {user_name}, i hope you're having a wonderful {day_time}")   # f-strings


welcome_msg("Megha", 400)

# checkout in-built functions at https://docs.python.org/3/library/functions.html#hex
# dictionaries
dict1 = {
    "name": "baby meggie",
    "age": 18,
    "job": "greatest artist of all time"
}
print(dict1["job"])
dict1["age"] += 1      # values can be modified
print(dict1["age"])

# tuples, lists that cannot be modified
tup = (1, 2, 5, 3, 69)
print(tup)

# sets. god knows why these exist.
set1 = {1, 2, 5, 6}   # or set1 = set([1, 2, 5, 6]). whyyyyyyyyyyyyyy.

# and that's about all the basics.
