# Treasure Island Game based on the choices of the user 
print("Welcome to Treasure Island.")
print("Your mission is to find the Treasure.")
road = input("You are at a cross road. Where do you want to go? Type 'left' or 'right' : ")
if road == 'right':
    print("You have been attacked by lions!! GAME OVER.")
else:
    lake = input("You came at a lake. There is an island in the middle of the lake. Type 'wait' to wait for the boat. Type 'swim' to swim across : ")
    if lake == 'swim':
        print("You are been eaten by crocodiles. GAME OVER")
    else:
        island = input("You arrived at an island unarmed. There is a house with three doors. One red, one yellow and one blue. Which one do you choose: ")
        if island == 'red' or island == 'blue':
            print("You are been eaten by Lions. GAME OVER")
        else:
            print("You found the Treasure , YOU WON")
