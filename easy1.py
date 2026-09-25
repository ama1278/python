num=int(input('enter ur number '))
if num%2==0:
    print('even')
else:
    print('odd') 


print('_-'*50)
num1=int(input('enter first number'))
num2=int(input('enter second number'))
if num1>num2:
    print(f'{num1} is bigger')
elif num1<num2:
    print(f'{num2} is bigger')
else:
    print("equal")

print('_-'*50)

grade=int(input('enter ur grade'))
if grade<100 and grade>=85:
    print('A')    
elif grade<85 and grade>=65:
    print('B')  
elif grade<65 and grade>=50:
    print('C')  
elif grade<50 and grade>=40:
    print('D')          
elif grade<40 and grade>=0:
    print('F')
else:
    print('out of range') 
                   
print('_-'*50)
 
age=int(input('how old are u'))
if age>18 and age>0:
    print('you are able to participate in election')
elif age<0:
    print('you entered wrong number')
else:
    print('u cant participate in election')
    
print('_-'*50)
   
def kabise(year):
    if year%4==0:
        return True
    if year%100==0:
        return False
    elif year%400==0:
        return True
yer=int(input('eter the year u want:  '))
if kabise(yer):
    print(f'{yer} is leap year')
else:
    print(f'{yer} is normal year')    
                            