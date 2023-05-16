import Day_14_projectart as Art
import Day_14_gamedata as Text
import random as r
import os


def description(index):
    """This function prints out the information of the random choice"""
    name = Text.data[index]['name']
    describe = Text.data[index]['description']
    country = Text.data[index]['country']
    desc = f"{name}, a {describe} from {country}"
    return desc


def compare(ch2, followers1, followers2, decision):
    """ this function compares the number of followers. and prints out a message accordingly
     it also returns either a 1 or a 0. which will be used to exit the game loop if you lose."""
    # print("reading")
    # print("followers1 : ",followers1)
    # print("followers2 : ",followers2)
    if decision == "lower":  # this to flip the numbers around. less code to write
        followers1, followers2 = followers2, followers1
        # print("lower check, swap")

    print("higher check")
    if followers1 <= followers2:
        print(f"you were correct! {Text.data[ch2]['name']} has {Text.data[ch2]['follower_count']} million followers")
        return 1
    else:
        # print("ch1 : ",ch1)
        # print("ch2 : ",ch2)
        print(f"you were wrong, {Text.data[ch2]['name']} has {Text.data[ch2]['follower_count']} million followers")
        return 0


def game():
    print(Art.logo)
    print(
        "Welcome to higher or lower. your goal is to guess the amount\nof instagram followers related to the person "
        "or entity on screen!")
    ch2 = r.randint(0, len(Text.data) - 1)
    score = 0
    while True:
        if score != 0:  # to always keep the logo on screen. this is so that
            print(Art.logo)  # it doesn't appear twice on the first round
        print(f"Your score : {score}")  # obviously score
        # print(len(text.data))
        ch1 = ch2  # second becomes first, and a new second entity is checked.
        ch2 = r.randint(0, len(Text.data) - 1)
        # print(ch1)
        # print(ch2)
        # print(text.data[ch1])
        # print(text.data[ch2])
        extra_text = f" with {Text.data[ch1]['follower_count']} million followers"  # to display number of followers
        print(description(ch1) + extra_text)  # but only for the first item
        print(Art.vs)
        print(description(ch2))
        choice = input("do you think this is higher or lower?\nMy decision : ")
        decision = compare(ch2, Text.data[ch1]['follower_count'], Text.data[ch2]['follower_count'], choice)
        if decision == 0:  # break game loop
            break
        score += 1
        input("press enter to continue")  # clear screen
        os.system('cls')

    print(f"You finished with a score of {score} points")  # final score message


game()
