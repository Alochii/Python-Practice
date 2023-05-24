# DONE: Create a letter using starting_letter.txt


with open("./Input/Letters/starting_letter.txt", "r+") as letter_file:
    letter_content = letter_file.read()

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()


for name in names:
    stripped_name = name.strip()
    new_letter = letter_content.replace("[name]", stripped_name)
    with open(f"./Output/ReadyToSend/letter for {stripped_name}", "w") as file:
        file.write(f"{new_letter}")
