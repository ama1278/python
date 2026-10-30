class Kasr:
        def __init__(kasr,soorat,makhraj):
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
        
              
Soorat,Makhraj=map(int,input("pls enter numbers").split())
Soorat1,Makhraj1=map(int,input("pls enter numbers").split())
if Makhraj==0:
        raise ZeroDivisionError
else:                    
        print(Kasr(Soorat,Makhraj).sadeh())                
        print((Kasr(Soorat,Makhraj,)).summ(Kasr(Soorat1,Makhraj1)))
        print(Kasr(Soorat,Makhraj).mult(Kasr(Soorat1,Makhraj1)))        
