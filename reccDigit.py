def sumOF_digit(num):
    summ=0
    if num<10:
        return num
    elif num>10:
        A=num%10
        summ=A+sumOF_digit(num//10)
        return summ
if (__name__)=='__main__':
    print(sumOF_digit(1234))    