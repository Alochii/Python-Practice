import turtle
import prettytable
"""
timmy = turtle.Turtle()
timmy.shape("turtle")
timmy.color("pink")
timmy.fd(120)
my_screen = turtle.Screen()
my_screen.exitonclick()
"""

table = prettytable.PrettyTable()
print(table)
table.field_names = ["pokemon", "type", "health", "defence"]
table.add_rows(
    [
        ["charmander","fire","500","300"],
        ["squirtel","water","600","250"],
        ["bulbasaur","grass","800","150"],
    ]
)

table.add_column("location",["kanto","forbidden city","your mom's basement"])
table.add_rows(
    [
        ["charmander","fire","500","300","s"],
        ["squirtel","water","600","250","s"],
        ["bulbasaur","grass","800","150",""],
    ]
)
table.align["location"] = "l"
table.align["pokemon"] = "l"
table.align["type"] = "l"
print(table)