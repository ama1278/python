class Kasr:
        def __init__(kasr,soorat,makhraj):
                if isinstance(soorat,int)==False or isinstance(makhraj,int)==False:
                        raise TypeError
                kasr.soorat=soorat
                kasr.makhraj=makhraj
                
        def gcd(kasr,soorat,makhraj):
                sooratt=[]
                makhrajj=[]
                mosh=[]
                biiggest=0
                for i in range(1,soorat+1): 
                        if soorat%i==0:
                                sooratt.append(i)
                for j in range(1,makhraj+1):
                        if makhraj%j==0:
                                makhrajj.append(j)
                for so in sooratt:
                        if so in makhrajj:
                                mosh.append(so)
                biiggest=max(mosh)                
                return biiggest                                
        def sadeh(kasr):
                gCd=kasr.gcd(kasr.soorat,kasr.makhraj)
                kasr.soorat//=gCd
                kasr.makhraj//=gCd
                return kasr
        def summ(kasr ,kasr1):
                makh=kasr.makhraj*kasr1.makhraj
                soo=(kasr.soorat*kasr1.makhraj) +(kasr1.soorat*kasr.makhraj)
                return Kasr(soo,makh).sadeh()
        def mult(kasr ,kasr1):
                makh=kasr.makhraj*kasr1.makhraj
                soo=(kasr.soorat*kasr1.soorat)
                return Kasr(soo,makh).sadeh()              
        def __str__(kasr):
                return f"{kasr.soorat}/{kasr.makhraj}"
def input_checker(a):
        checker=input(a).split()        
        if len(checker)==2:
                return int(checker[0]), int(checker[1])
        else:
                raise ValueError('you can jst enter two variables')
Soorat,Makhraj=input_checker('enter youre numbers ')
Soorat1,Makhraj1=input_checker('enter ur numbers')
if Makhraj==0 or Makhraj1==0:
        raise ZeroDivisionError
else:                    
        print(Kasr(Soorat,Makhraj).sadeh())                
        print((Kasr(Soorat,Makhraj,)).summ(Kasr(Soorat1,Makhraj1)))
        print(Kasr(Soorat,Makhraj).mult(Kasr(Soorat1,Makhraj1)))        
