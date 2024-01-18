print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Logic for game
def start_game():
    print("Welcome to Treasure Island. Your mission is to find the treasure.")
    first = input("You've encountered a crossroad, choose a direction to go. (Type Left or Right to get started.): ")

    if first.casefold() == "left":
        second = input('You have arrived at an ocean. There is an island in the middle of the ocean. Type "wait" if you would like to wait for a boat. Type "swim" if you would like to swim. ')
        if second.casefold() == "wait":
            third = input("You've arrived at the island unharmed. There are 3 doors. Each has a different color: Red, Yellow, and Blue. Choose the correct door. ")
            if third.casefold() == "yellow":
                print("You win!")
            elif third.casefold() == "blue":
                print("Eaten by beasts. Game Over.")
                start_game()
            elif third.casefold() == "red":
                print("Burned by fire. Game Over.")
                start_game()
            else:
                print("Game Over.")
                start_game()
        else:
            print("Attacked by trout. Game Over.")
            start_game()
    else:
        print("You've fallen into a hole. Game Over.")
        start_game()

start_game()                                      