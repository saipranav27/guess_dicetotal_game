from random import randint
from time import sleep
def get_user_guess():
  guess = int(input("Enter the guess"))
  return guess
def roll_dice(number_of_sides):
  first_roll=randint(1, number_of_sides)
  second_roll=randint(1, number_of_sides)
  max_value = number_of_sides * 2
  print ("The max_value is %d" % max_value)
  guess= get_user_guess()
  if max_value < guess:
    print("Guess is Invalid")
  else:
    print("Rolling")
    sleep(2)
    print("The outcome of first roll is %d" % first_roll)
    sleep(1)
    print("The outcome of Second roll is %d" % second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print("The Total roll: %d" % total_roll)
    print("Result...")
    sleep(1)
    if guess == total_roll:
      print("You Win")
    else: 
      print("You Lost")
roll_dice(6)
        
        
    
        
        

    