def reversed_of(number):
    reverseD=0
    s=len(str(number))
    for i in range(s):
        digits=number%10
        reverseD=(reverseD*10)+digits
        number=number//10
    return reverseD
# num=int(input('gimme your number:  '))
# print(reversed_of(num))    
        