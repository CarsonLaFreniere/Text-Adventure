# Carson, Assignment 1, gameFile.py

import inventory
import map

def runGame():
    import map
    name = input("What is your characters name? ")
    print("Welcome " + name + " to the game")
    map.ExistIn0_0()
    commandList()

def commandList():
    commands = {
        "look": map.Look,
        "move": map.Move,
        "take": map.Take,
        "use" : inventory.useItem,
        "inventory": inventory.displayInventory,
        "exit": map.Exit
    }

    while True:

        print()

        userInput = input("What do you want to do? (look, move, take, inventory, use, exit) ")
        if userInput in commands:
            commands[userInput]() 
        else:
            print(userInput + " is not a command")

runGame()