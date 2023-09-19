import turtle
import pandas
screen = turtle.Screen()
pic_turtle = turtle.Turtle()
picture = "blank_states_img.gif"
turtle.addshape(picture)
pic_turtle.shape(picture)

# def clickonscreen(x,y):
#     print(x,y)
# screen.onclick(clickonscreen)
def writing_turtle(x, y, state):
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.speed(0)
    writer.penup()
    writer.goto(x,y)
    writer.write(state,align="center")

states_found = []
score = 0
while True :
    state_guess = turtle.textinput("States memorizing game",f"guess the name of a state! {score}/50").title()
    data = pandas.read_csv("50_states.csv")
    if state_guess == "Exit":
        break
    if state_guess in data.state.unique() and state_guess not in states_found:
        states_found.append(state_guess)
        print(state_guess in data.state.unique())
        x_position = int(data[data.state == state_guess].x)
        y_position = int(data[data.state == state_guess].y)
        writing_turtle(x_position, y_position, state_guess)
        score += 1
    if score == 50 :
        print("you won!")
        break

states_list = data.state.tolist()
for state in states_found:
    states_list.remove(state)
print(states_list)
state_dictionary = {
    "states": states_list,
}
states_csv = pandas.DataFrame(state_dictionary)
states_csv.to_csv("states yet to be learned")