num=int(input('enter your number '))
s=len(str(num))
reverse=0
for i in range(s):
    digits=num%10
    reverse=(reverse*10 )+digits
    num=num//10
print(reverse)    
    