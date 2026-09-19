def Is_perfect(number):
    count=0
    for i in range(1,number):
        if number%i==0:
            count+=i
    if count==number:
        return True
    else:
        return False
numm=int(input("gimme your number:  "))  
if Is_perfect(numm):
    print(f'{numm} is perfect')
else:
    print(f"{numm} is not perfect")                  