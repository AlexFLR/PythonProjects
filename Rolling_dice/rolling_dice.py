import random


def rolling_dice():
     list=(1,2,3,4,5,6)
     random_dice_number =random.choice(list)
     # stop_the_program = False
     message = input('Do u want to roll the dice (y/n) ?') == 'y'
     
     if message:
          print(f'The number is {random_dice_number} ')
     
     message_2 = input('Do u want to roll the dice again (y/n) ?') == 'y'
     while message_2 ='y':
     





          # message = input('Do u want to roll the dice (y/n) ?') == 'y'
          # message_2 = input('Do u want to roll the dice again (y/n) ?') == 'y'
          
          # if message:
          #      print(f'The number is {random_dice_number}')
          #      print(message_2)
          # elif message_2:
          #      print(f'You number is {random_dice_number}')
          #      message_2=input()
               
     
   
         

     

rolling_dice()