import random as rn
Choices=['rock','paper','scissors']
computer=rn.choice(Choices)
player=input('enter ur choice')
if player==computer:
    print('draw')
    player=input('enter ur choice')
    