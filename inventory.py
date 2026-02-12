# Carson, Assignment 1, inventory.py

hasSticksAndStones = False
hasWaterAndFood = False
hasLongSword = False
hasShieldOfAchilles = False
hasGoldBars = False
hasWingsOfIcarus = False
hasWatch = False
hasTopHat = False
hasSkull = False
hasGoldPot = False
hasDiamond = False

def displayInventory():
    print("Here is your Inventory!")
    isEmpty = True
    if hasWatch:
        print("- A shiny Watch")
        isEmpty = False
    if hasSticksAndStones:
        print("- Sticks and Stones")
        isEmpty = False
    if hasWaterAndFood:
        print("- Rations of Food and Water")
        isEmpty = False
    if hasLongSword:
        print("- A sturdy Long Sword")
        isEmpty = False
    if hasShieldOfAchilles:
        print("- The legendary Shield of Achilles")
        isEmpty = False
    if hasGoldBars:
        print("- 50,000 pounds of Pure Gold Bars!")
        isEmpty = False
    if hasWingsOfIcarus:
        print("- Wings of Icarus (Handle with care near the sun)")
        isEmpty = False
    if hasTopHat:
        print("- Abe Lincoln's Golden Top Hat")
        isEmpty = False
    if hasSkull:
        print("- Jeweled Skull")
        isEmpty = False
    if hasGoldPot:
        print("- Pot of Gold")
        isEmpty = False
    if hasDiamond:
        print("- 24 Carrot Diamond")
        isEmpty = False
    if isEmpty:
        print("- Your inventory is empty.")

def useItem():
    if hasWingsOfIcarus:
        confirm = input("Are you sure you would like to use the Wings of Icarus (y/N)" )
        if confirm == "y":
            useLocation = input("The Wings of Icarus let you fly anywhere you want. Where would you like to go?")
            print("Fantastic choice! Moving to " + useLocation)
    elif hasWaterAndFood:
        confirm = input("Do you want to use some rations of Food and Water? (y/N) ")
        if confirm == "y":
            print("The food you ate expired 2000 years ago, you died of food poisoning")
            print("Game Over")
            exit()
        else:
            print("Saving Rations")