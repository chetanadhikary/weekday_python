##x = 5
##if x > 5:
##    print('X is greater than 5')
##print('X is ',x)

##x = int(input('Enter a number'))

##if x >= 0:
##    print('X is a positive number')
##    if x >= 1:
##        print('X is a non zero number')
##    else:
##        print('X is zero')
##else:
##    print('X is a negative number')
##
##

##if x == 0 :
##    print('X is a positive number')
##elif x >= 0:
##    print('X is non-zero positive number')
##else:
##    print('X is a negative number')

##    
##if (x >= 0) or (x>=1):
##    print('X is not zero ')
##else:
##    print('X is a negative number')
##


## Write a program which takes three inputs, and
## get the largest of the three numbers
##
##numbers = input('Enter three numbers seperated by comma\n')
##lst_num = numbers.split(',')
##x = int(lst_num[0])
##y = int(lst_num[1])
##z = int(lst_num[2])
##print(f'The input numbers are {x},{y},{z}')
##
##if x>y :
##    if x>z:
##        print(f'{x} is the largest number')
##    else:
##        print(f'{z} is the largest number')
##else:
##    if y>z:
##        print(f'{y} is the largest number')
##    else:
##        print(f'{z} is the largest number')
##


## Conditional Statements on strings
##
##name = input('Enter your name')
##lst_name = name.split(' ')
##if len(lst_name) > 1:
##    print(f'Your first name is {lst_name[0]}')
##    print(f'Your last name is {lst_name[1]}')
##else:
##    print(f'Your name is {name}')
##          
## We need authenticate an email id .
##    You need to check for the character '@'
## print the username of the the account

email = input('Enter your email ID')
if '@' in email:
    username = email.split('@')[0]
    print(f'The user name is found to be {username}')
else:
    print('Email is not valid')










