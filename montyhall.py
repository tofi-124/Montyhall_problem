import random


def game(inp):

    cargoat = ["car", "goat", "goat"]
    doors = {
        "a": "",
        "b": "",
        "c": "",
    }

    random.shuffle(cargoat)

    x = 0

    for door in doors:
        doors[door] = cargoat[x]
        x = x + 1

    playerchoice = doors[inp]
    del doors[inp]

    for door in doors:
        if doors[door] == "goat":
            print(f"Behind {door} exists a goat")
            del doors[door]
            break

    inp = input("do you want to swap or stick with your choice? y or n > ")
    if inp == "y":
        playerchoice = str(doors.values())

    print(f"The choices were {cargoat}")

    if playerchoice == "car":
        print("you win")
    else:
        print("you lose!")


inp = input(
    "you're given the choice of three doors:\nBehind one door is a car; \nbehind the others, goats. chose a, b or c > "
)
game(inp)

