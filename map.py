# Carson, Assignment 1, map.py

import random
import inventory
import time

location = "0_0"
chestLooted = False

def ExistIn0_0():
    global location
    location = "0_0"

def ExistIn0_1():
    global location
    location = "0_1"

def ExistIn1_0():
    global location
    location = "1_0"

def ExistIn1_1():
    global location
    location = "1_1"

def ExistIn1_2():
    global location
    location = "1_2"

def ExistIn2_1():
    global location
    location = "2_1"
    
def ExistIn2_2():
    global location
    location = "2_2"

def ExistInSecret():
    global location
    location = "secret"

def Look():
    global location
    if location == "0_0":
        print("You look around. You see the leaves glistening off the sun, the water clear as day. You are in the Aetherwoods. To the North and West are Ancient Rock Walls. To your South and East you see an opening. Inside one of the trees you see the faint glistening on a Treasure Chest.")
        print("")
        time.sleep(2)
        Take()
    elif location == "0_1":
        print("You end up inside of a Cave. It's pitch black, you can't see anything. You hear creepy noises and think you saw something fly by. You can see the light North.")
        print("")
    elif location == "1_0":
        print("As you exit the Cave you look around and see a giant mountain North. The waves are splashing along the sandy beach East, You hear the water flowing West.")
        print("")
    elif location == "1_1":
        print("As you follow the river West you end up finding yourself peering over a 50 foot canyon in the ground. To your right is Abe Lincoln's golden top hat")
        print("")
        time.sleep(2)
        Take()
        time.sleep(2)
        print("There are paths to the North, South, and East")
        print("")
    elif location == "1_2":
        print("As you exit the cannyon a swampy forest appears in your vision, something tells you it's a bad idea but you go to it anyways. You take your first step into the swamp and end up getting stuck in the muck. As you are digging yourself out, you find a Jeweled skull.")
        print("")
        time.sleep(2)
        print("Something is faintly glowing to the West, it's a mysterious Witch Portal. To the North and East are path that lead through the Swamp.")
        print("")
        time.sleep(2)
        Take()
    elif location == "2_1":
        print("Upon exiting the Swamp, you see a vast wasteland of what seems to be an exploded volcano. At the top of a pile of ash, you see a big 24 carrot Diamond.")
        print("")
        time.sleep(2)
        Take()
        time.sleep(2)
        print("There are paths leading outside of the volcanic wasteland to the west and south, to the North you hear the waves splashing from the Ocean.")
        print("")
    elif location == "2_2":
        print("The Volcanic Wasteland path lead to a massive grass plain. Over in the distance you see a rainbow... Not just a rainbow, THE END OF THE RAINBOW!")
        print("")
        confirm = input("Do you want to follow the Rainbow? (y/N) ")
        if confirm == "y":
            print("Following the Rainbow")
            print("")
            time.sleep(10)
            print("Were almost there")
            print("")
            time.sleep(5)
            print("It's fading away. WAIT I SEE SOMETHING")
            print("")
            time.sleep(2)
            print("The rumors are true, there is a pot of gold at the end of a Rainbow")
            print("")
            Take()
            time.sleep(2)
            print("Heading back to the Path")
            print("")
        else:
            print("There's never anything at the end of a Rainbow")
            print("")
        time.sleep(5)
        print("")
        print("Towards the East there is a huge chasm in the ground. West and North are both Paths. Towards the South there is a Magical Glowing Exit.")
        print("")


def Move():
    global location
    direction = input("Which direction? ").lower()
    
    if location == "0_0":
        if direction == "north":
            print("Ouch, You stubbed your toe on the Rock Wall.")
            print("")
        elif direction == "west":
            print("Ouch, You stubbed your toe on the Rock Wall.")
            print("")
        elif direction == "east":
            print("Entering the Cave")
            print("")
            ExistIn0_1()
        elif direction == "south":
            print("Entering the Cave")
            print("")
            ExistIn0_1()
        else:
            print(direction + " is not a Direction")
            print("")
            
    elif location == "0_1":
        if direction == "north":
            print("Exiting the Cave")
            print("")
            ExistIn1_0()
        else:
            print("You went the wrong way and a massive grue devoured you alive")
            print("")
            time.sleep(2)
            print("Game Over :(")
            print("")
            time.sleep(2)
            exit()

    elif location == "1_0":
        if direction == "north":
            print("You tried climbing the mountain but held onto the wrong rock and it broke as you fell to the ground. Let's not try that again")
            print("")
        elif direction == "east":
            print("It's really hot out, the water looks so refreshing. As you finish your swim and heading back you see the reflection of the sun from something in the ground, it's a watch!")
            print("")
            time.sleep(1)
            Take()
            time.sleep(1)
            print("Heading back to the Cave")
            print("")
        elif direction == "south":
            print("Back into the cave we go.")
            print("")
            ExistIn0_1()
        elif direction == "west":
            print("Following the water stream sounds like a good idea!")
            print("")
            ExistIn1_1()
        else:
            print(direction + " is not a Direction")
            print("")

    elif location == "1_1":
        if direction == "west":
            if inventory.hasTopHat == True:
                print("The Top Hat had a spider collony living inside of it and you threw the hat away and tripped backwards plummeting 50 feet into the cannyon and died.")
                print("")
                time.sleep(2)
                print("Game Over :(")
                print("")
                time.sleep(2)
                exit()
            else:
                print("The ground your standing on begins to give out and you fall 50 feet down the cannyon and die.")
                print("")
                time.sleep(2)
                print("Game Over :(")
                print("")
                time.sleep(2)
                exit()
        elif direction == "north" or direction == "south" or direction == "east":
            print("Leaving the cannyon")
            print("")
            ExistIn1_2()
        else:
            print(direction + " is not a Direction")
            print("")
            
    elif location == "1_2":
        if direction == "west":
            print("Moving towards the Portal")
            print("")
            time.sleep(1)
            print("")
            time.sleep(1)
            confirm = input("The portal looks broken and worn down, Would you like to still enter? (y/N)")
            if confirm == "y":
                ExistIn0_0()
            else:
                print("I probably shouldn't go through a broken portal")
                print("")
                Move()
        elif direction == "north":
            print("Navigating the Swamp")
            print("")
            time.sleep(3)
            print("Finally, I see the exit")
            print("")
            ExistIn2_1()
        elif direction == "east":
            print("Navigating the Swamp")
            print("")
            time.sleep(3)
            ExistIn2_1()
            print("Finally, I see the exit")
            print("")
        elif direction == "south":
            print("This seems to be the end of the world. You cannot go that way")
            print("")
            Move()
        else:
            print(direction + " is not a Direction")
            print("")
            
    elif location == "2_1":
        if direction == "north":
            print("Arriving at the ocean, you see the Loch Ness Monster.")
            print("")
            time.sleep(5)
            print("In complete shock you freeze for 5 seconds. You end up getting it together and run the other way after wetting your pants a bit.")
            print("")
        elif direction == "west":
            print("Leaving the Wasteland")
            print("")
            ExistIn2_2()
        elif direction == "south":
            print("Leaving the Wasteland")
            print("")
            ExistIn2_2()
        elif direction == "east":
            print("Ah shucks! You forgot your skis at home :( Looks like we wont be sking today.")
            print("")
        else:
            print(direction + " is not a Direction")
            print("")
            
    elif location == "2_2":
        if direction == "east":
            print("As you approach the Huge Chasm, you think to yourself; I wonder if theres water in the bottom?")
            print("")
            time.sleep(2)
            confirm = input("Do you want to find out? (y/N)")
            print("")
            if confirm == "y":
                print("As you attemp to swan dive into the huge chasm wondering if theres water in the bottom, You Die.")
                print("")
                time.sleep(2)
                print("Game Over :(")
                print("")
                exit()
            else:
                print("I have more control over my intrusive thoughts and won't swan dive into the chasm.")
                print("")
        elif direction == "west":
            print("Following the Path")
            print("")
            time.sleep(60)
            print("Still following the Path")
            print("")
            time.sleep(300)
            print("How long is this Path?")
            print("")
            time.sleep(900)
            print("Wow! This is a really long Path")
            print("")
            time.sleep(3600)
            print("Why are you still here?")
            print("")
            time.sleep(43200)
            help = input("Do you need help? (y/N)")
            print("")
            if help == "y":
                print("Please call 911")
                print("")
            else:
                print("You must be really tired!")
                print("")
            time.sleep(86400)
            print("You need help. Please call any help line right now.")
            print("")
            time.sleep(360)
            print("You reached the Secret Area.")
            print("")
            ExistInSecret()
        elif direction == "north":
            print("Following the Path")
            print("")
            time.sleep(60)
            print("Still following the Path")
            print("")
            time.sleep(300)
            print("How long is this Path?")
            print("")
            time.sleep(900)
            print("Wow! This is a really long Path")
            print("")
            time.sleep(3600)
            print("Why are you still here?")
            print("")
            time.sleep(43200)
            help = input("Do you need help? (y/N)")
            print("")
            if help == "y":
                print("Please call 911")
                print("")
            else:
                print("You must be really tired!")
                print("")
            time.sleep(86400)
            print("You need help. Please call any help line right now.")
            print("")
            time.sleep(360)
            print("You reached the Secret Area.")
            print("")
            ExistInSecret()
        elif direction == "south":
            print("Congratulations, you completed The Game!")
            print("")
            time.sleep(2)
            print("")
            inventory.displayInventory()
            time.sleep(1)
            exit()
        elif direction == "north":
            print("Following the Path")
            print("")
            ExistIn2_1()
        else:
            print(direction + " is not a Direction")
            print("")

def chestLoot(): # https://www.w3schools.com/python/ref_random_choices.asp
    items = [
        "Nothing",
        "Sticks and Stones",
        "Water and food",
        "Long Sword",
        "Shield of Achilles",
        "50,000 pounds of Pure Gold Bars",
        "Wings of Icarus"
    ]
    itemWeights = [
        45.0,
        25.0,
        11.5,
        15.0,
        2.5,
        1.5,
        0.5
    ]
    
    lootItem = random.choices(items, itemWeights, k=1)
    return lootItem[0]


def Take():
    global chestLooted
    global location
    taking = input("Would you like to take it? (y/N) ")
    
    if taking == "y":
        if location == "0_0":
            if chestLooted == False:
                item = chestLoot()
                chestLooted = True
                print("You opened the Treasure Chest and inside found " + item)
                print("")

                if item == "Sticks and Stones":
                    inventory.hasSticksAndStones = True
                elif item == "Water and food":
                    inventory.hasWaterAndFood = True
                elif item == "Long Sword":
                    inventory.hasLongSword = True
                elif item == "Shield of Achilles":
                    inventory.hasShieldOfAchilles = True
                elif item == "50,000 pounds of Pure Gold Bars":
                    inventory.hasGoldBars = True
                elif item == "Wings of Icarus":
                    inventory.hasWingsOfIcarus = True
            else:
                print("You already looted this chest silly")
                print("")
            
        elif location == "1_0":
            print("You pick up the watch.")
            print("")
            inventory.hasWatch = True
        elif location == "1_1":
            print("You stole Abe Lincoln's golden top hat")
            print("")
            inventory.hasTopHat = True
        elif location == "1_2":
            print("Sweet! A skull covered in Jewels, this can be worth MILLIONS!!")
            print("")
            inventory.hasSkull = True
        elif location == "2_1":
            print("This Diamond is worth so much Money!")
            print("")
            inventory.hasDiamond = True
        elif location == "2_2":
            print("This pot of gold is so heavy! Let's hop theres no lepercaun's around")
            print("")
            inventory.hasGoldPot = True
        else:
            print("There is nothing here to take.")
            print("")
    else:
        print("No taking today.")
        print("")


def Exit():
    confirm = input("Are you sure you want to Exit the game? (y/N) ")
    if confirm == 'y':
        print("Leaving game")
        print("")
        exit()
    else:
        print("No exiting.")
        print("")