def divide(num1,num2):
    if num1<num2:
        return 0
    return 1+divide(num1-num2,num2)
if (__name__)=='__main__':
    print(divide(200,2))
  