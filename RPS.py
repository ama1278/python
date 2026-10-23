import random as rn
Choices=['rock','paper','scissors']
computer=rn.choice(Choices)
player=input('enter ur choice (rock , paper or scissors)')
if player==computer:
    print('draw')
elif player=="rock"and computer=='scissors':
    print('player win')
elif player=="scissors"and computer=='paper':
    print('player win')    
elif player=="paper"and computer=='rock':
    print('player win')
elif player=="rock"and computer=='paper':
    print('computer win')
elif player=="scissors"and computer=='rock':
    print('computer win')        
elif player=="paper"and computer=='scissors':
    print('computer win')    
else:
    print('invalid choice')    
    