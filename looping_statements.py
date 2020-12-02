## Looping Statements
x = 10
##
##while x > 0:
##    print(x)
##    x -= 1
##else:
##    print(f'Out of the loop value x:{x}')

##
##while x > 0 :
##    x -= 1
##    if x%2 == 0:
##        print(x)
##    else:
##        continue
##else:
##    print(f'Out of the loop value x:{x}')

##
##while True :
##    x -= 1
##    if x > 0:
##        if x%2 == 0:
##            print(x)
##        else:
##            continue
##    else:
##        break
##else:
##    print(f'Out of the loop value x:{x}')
##



## Write a program which will accept the user number and add to a list if its even
## If user inputs an alphabet/string the program should exit printing the list
##
##lst_even = []
##lst_odd = []
##while True:
##    value_ = input('Enter a number to check')
##    if value_.isdigit():
##        if int(value_)%2 == 0:
##            lst_even.append(value_)
##        else:
##            lst_odd.append(value_)
##    else:
##        print(f'even list:{lst_even}\nodd list:{lst_odd}')
##        break



lst_numbers = [1,2,3,4,5,6,23,239]
lst_sq = []
i = 0
while i < len(lst_numbers):
    sq_num = lst_numbers[i]**2
    lst_sq.append(sq_num)
    i += 1
else:
    print(f'Using while loop:{lst_sq}')

lst_sq_f = []
for num in lst_numbers:
    lst_sq_f.append(num**2)
else:
    print(f'Using for loop:{lst_sq_f}')



## Write a program which will accept the user number and add to a list 
## If user inputs an alphabet/string the program should exit printing the list
## Calculate the sum of the numbers,maximum of the numbers, minimum of the numbers





