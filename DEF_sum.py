def summ():
    Summ=0
    count=int(input('how many numbers u want to sum up? '))
    for i in range(count):
        numbers=int(input('enter ur numbers u want to sum up: '))
        Summ+=numbers
    return Summ    
print(summ())
     