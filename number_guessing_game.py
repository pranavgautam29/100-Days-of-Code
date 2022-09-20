import random
random_number = random.randint(0,100)
def easy_level():
    print("You have 10 chances to make the right guess.")
    number_of_attempts = 10
    should_continue = True
    while should_continue:
        guess = int(input("Make a guess:"))
        if random_number > guess:
            print("Try guessing a higher number.")
            print("You have",number_of_attempts-1,"attempts left.")  
        elif random_number < guess:
            print("Try guessing a lower number.")
            print("You have",number_of_attempts-1,"attempts left.")  
        else:
            print("You guessed it right")
            break
        number_of_attempts -=1
        if number_of_attempts == 0 :
            print("You lose, the number was:",random_number)
            should_continue = False
def hard_level():
    print("You have 5 chances to make the right guess.")
    number_of_attempts = 5
    should_continue = True
    while should_continue:
        guess = int(input("Make a guess:"))
        if random_number > guess:
            print("Try guessing a higher number.")
            print("You have",number_of_attempts-1,"attempts left.")        
        elif random_number < guess:
            print("Try guessing a lower number.")
            print("You have",number_of_attempts-1,"attempts left.")  

        else:
            print("You guessed it right")
            break
        number_of_attempts -=1
        if number_of_attempts == 0 :
            print("You lose, the number was:",random_number)
            should_continue = False
print("Welcome to Number Guessing Game!!")
print("Guess a number between 0 and 100")
user_choice = input("Select a level. Easy or Hard:").lower()
if user_choice  == 'easy':
    easy_level()
elif user_choice =='hard':
    hard_level()
else:
    print("Invalid Input")