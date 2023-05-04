
#importing modules


import random
import string

def generate_password(min_length, numbers=True, special_characters=True):
    letters= string.ascii_letters # ascii lowercase+ ascii uppercase
    digits = string.digits  # digits (0,1,2...)
    special = string.punctuation #(every punctuation symbol : !,?,&,%)

    characters = letters
    if numbers: # numbers=True when we do not have a condition
        characters+=digits
    if special_characters:
        characters+=special
    
    pwd = ''
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters) #returns a random value from the specified sequence
        pwd +=new_char
        
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True
        
        meets_criteria = True
        if numbers:
            meets_criteria= has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd.title()  


min_length = int(input('Enter the minimum length: '))
has_number = input('Do u want to have numbers (y/n)?').lower() =='y'
has_special = input('Do u want to have special characters (y/n)?').lower() =='y'

pwd = generate_password(min_length,has_number,has_special)
print('The generated password is: ',pwd)

