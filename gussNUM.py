import random as rn
a=rn.randint(1,101)
while (num:= int(input('please enter ur number'))) != a:
    if a>num:
        print('ur number was lower ')
    elif a<num:
        print('ur number was bigger')
    else:
        print('correct guess!!! congrats')        