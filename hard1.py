def is_prime(numm):
    flag=0
    for n in range(2,numm):
        if numm%n==0:
            flag+=1
    if flag==0:
        return True
    else:
        return False

#=====================palindrome======================================
def pal(item):  
    if item==item[::-1]:
        return True
    else:
        return False
