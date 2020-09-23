#!/usr/bin/env python
# coding: utf-8

# In[5]:


from time import sleep
from random import randint 


def header(name):
    print(f"++++++++++++++\n{name}\n++++++++++++++")

def roll_dice():
    kit = randint(1,6)
    return kit  


def show_dice(value, value2):
    return f"Rolled a {value} and a {value2}"
   

def dice_value():
    kit = roll_dice()
    ken = roll_dice()
    print(show_dice(kit, kit))
    return kit + ken


    
def print_end_game_status(user_hand_sum, dealer_hand_sum):
    header('GAME RESULT')

    if user_hand_sum <= 50 and (user_hand_sum > dealer_hand_sum or dealer_hand_sum > 50):
        print('You win!')
    elif dealer_hand_sum <= 50 and (dealer_hand_sum > user_hand_sum or user_hand_sum > 50):
        print('Luda wins!')
    else:
        print('Tie.')

def open_statement(name):
    statement = f"Hello {name}.\nYour about to play LudoRoute"
    print(statement)
    
def response():
    return input("START or HELP?\nIf you need help type 'help' to view the game discription; else type 'start' to begin.\n")
    
def ludo_remark(hand_sum): 
    if hand_sum in range(45, 50):
        response = "In house!"
    elif hand_sum == 50:
        response = "LUDOKING!"
    elif hand_sum > 50:
        response = 'LOOTED.'
    else:
        response = ''
    print(response)      
    
    
def roll_dice():
    return randint(1,6)
      


def show_dice(value, value2):
    return f"Rolled a {value} and a {value2}"
   

def dice_value():
    die1 = roll_dice()
    die2 = roll_dice()
    print(show_dice(die1, die2))
    return die1 + die2


# In[ ]:





# In[6]:


#game comments
name = input("What is your name?")
open_statement(name)
play_game = response().lower()

while play_game == 'help':
    print("LudoRoute is a game that mutates Ludo. The player is given an option to roll curb, a curb contains two dice, each die have 6 faces, with value 1, 2, 3, 4, 5, and 6. open the user link start game")
    play_game = response().lower()
   
print('')

print("Game will start in ")
for i in [3, 2,1]:
    print(i)
    sleep(1)
    
print("Begin!\n")   
header(name + ', your TURN')

user_hand_sum = 0
for i in range(4):
    user_hand_sum += dice_value()
    print(f"Hand value = {user_hand_sum}")


yes_no = input("Roll the dice, YES or NO?").lower()    
while yes_no == 'yes' and user_hand_sum < 50:
    user_hand_sum += dice_value()
    print(f"Hand value = {user_hand_sum}")
    if user_hand_sum < 50:
        yes_no = input("Roll the dice, YES or NO?").lower()    
if yes_no == 'no':
    print(f"{name}, your final hand value is {user_hand_sum}") 
    
ludo_remark(user_hand_sum)  

print('')
header("Luda's TURN")

dealer_hand_sum = 0
while dealer_hand_sum <= 45:
    dealer_hand_sum += dice_value()
    
print("Luda's final is {}".format(dealer_hand_sum))
ludo_remark(dealer_hand_sum) 
print(' ')


print_end_game_status(user_hand_sum, dealer_hand_sum)


# In[ ]:





# In[ ]:




