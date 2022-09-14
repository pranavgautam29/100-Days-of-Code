import random
choices = ["rock", "paper", "scissor"]
choice_index = random.randint(0, 2)
computer_choice = choices[choice_index]
player_choice = int(
    input("Please press 0 for rock, 1 for paper or 2 for scissors: "))

if choice_index == player_choice:
    print("Computer chose:", computer_choice)
    print("You chose:", choices[player_choice])
    print("Its a Draw!")
elif choice_index == 0 and player_choice == 1:
    print("Computer chose:", computer_choice)
    print("You chose:", choices[player_choice])
    print("You won!")
elif choice_index == 0 and player_choice == 2:
    print("Computer chose:", computer_choice)
    print("You chose:", choices[player_choice])
    print("Computer won!")
elif choice_index == 1 and player_choice == 0:
    print("Computer chose:", computer_choice)
    print("You chose:", choices[player_choice])
    print("Computer won!")
elif choice_index == 1 and player_choice == 2:
    print("Computer chose:", computer_choice)
    print("You chose:", choices[player_choice])
    print("You won!")
elif choice_index == 2 and player_choice == 0:
    print("Computer chose:", computer_choice)
    print("You chose:", choices[player_choice])
    print("You won!")
elif choice_index == 2 and player_choice == 1:
    print("Computer chose:", computer_choice)
    print("You chose:", choices[player_choice])
    print("Computer won!")
else:
    print("You typed something Invalid!")
