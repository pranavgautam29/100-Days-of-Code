import random
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def random_cards(cards):
    return random.choice(cards)
player_cards = []
computer_cards = []
for i in range(2):
    player_cards.append(random_cards(cards))
computer_cards.append(random_cards(cards))

play_again = True
def sum_cards(cards):
    sum = 0
    for i in cards :
        sum += i
    return sum
while play_again:
    print("Your cards:",player_cards,"Current score:",sum_cards(player_cards))
    print("Computers cards:",computer_cards)
    player_choice = input("Type 'y' to get another card or 'n' to pass:") 
    if player_choice == 'y':
        player_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
    elif player_choice == 'n':
        computer_cards.append(random.choice(cards))
    else:
        print("Invalid Input!!")
    player_sum = sum_cards(player_cards)
    computer_sum = sum_cards(computer_cards)
    print("Your final hand:",player_cards)
    print("Computer's final hand:",computer_cards)
    if player_sum > 21:
        print("Computer Won!")
    elif computer_sum > 21:
        print("You Won!!")
    elif computer_sum == player_sum:
        print("Its a Draw")
    else:
        if player_sum > computer_sum:
            print("You Won!!")
        elif player_sum < computer_sum:
            print("Computer Won!!")
    if input("Do you want to play again(y or n):") == 'n':
        print("GoodBye!!")
        play_again = False




