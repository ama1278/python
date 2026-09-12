num1=int(input('pls enter a number'))
num2=int(input('pls enter a number'))

for i in range(num1,num2+1):
    if num1<0 and num2<0:
        continue
    flag=0
    for j in range(1,i):
        if i%j==0:
            flag+=j
    if flag==i:
        print(flag)            
          
            