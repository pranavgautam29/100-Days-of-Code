print("Welcome to HangMan!!")
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
stages.reverse()
end_of_game = False
import random
words = words = ('ant baboon badger bat bear beaver camel cat clam cobra cougar '
         'coyote crow deer dog donkey duck eagle ferret fox frog goat '
         'goose hawk lion lizard llama mole monkey moose mouse mule newt '
         'otter owl panda parrot pigeon python rabbit ram rat raven '
         'rhino salmon seal shark sheep skunk sloth snake spider '
         'stork swan tiger toad trout turkey turtle weasel whale wolf '
         'wombat zebra ').split()
random_word = random.choice(words)
blanks = []
for i in range(len(random_word)):
    blanks.append("_")
max_lives = 6


while not end_of_game:
        user_guess = input("Guess a letter:").lower()
        for position in range(len(random_word)):
            letter = random_word[position]
            if user_guess == letter:
                blanks[position] = user_guess
        print(blanks)
        if user_guess not in random_word:
            max_lives -= 1
            print("You guessed",user_guess,"that's not in the word.")
            print(stages[max_lives])


        if max_lives == 0 or '_' not in blanks:
            end_of_game = True
            
if max_lives > 0:
    print("You Win")
else:
    print("You Lose!! The word was",random_word)    
    






