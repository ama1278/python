def gcd(soorat,makhraj):
        sooratt=[]
        makhrajj=[]
        mosh=[]
        for i in range(1,soorat+1): 
                if soorat%i==0:
                        sooratt.append(i)
        for j in range(1,makhraj+1):
                if makhraj%j==0:
                        makhrajj.append(j)
        for so in sooratt:
                if so in makhrajj:  
                        mosh.append(i)
        return max(mosh)

print(gcd(50,100))