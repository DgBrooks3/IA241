# Lab 5 if Statements

# 3.1
alien_color = 'green'

if alien_color == 'green':
    print('You have earned 5 points!')

# 3.2
alien_color = 'red'
if alien_color == 'green':
    print('You have earned 5 points for shooting the alien!')
else:
    print('You have earned 10 points!')

# 3.3
favorite_fruits = ['avocados', 'grapes', 'oranges']
if 'grapes' in favorite_fruits:
    print('Wow, you really like grapes!')
    
if 'bananas' in favorite_fruits:
    print('Wow, you really like bananas!')
    
if 'apples' in favorite_fruits:
    print('Wow, you really like apples!')

# 3.4
age = 19
if age < 10:
    print('Looks like you are a child.')
elif age >= 10 and age < 20:
    print('Looks like you are a teenager.')
elif age >= 20 and age < 65:
    print('Looks like you are an adult.')
else:
    print('Looks like you are an elder.')