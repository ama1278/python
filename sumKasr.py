class Kasr:
        def __init__(kasr,soorat,makhraj):
                kasr.__soorat=soorat
                kasr.__makhraj=makhraj
        @property
        def makhraj(kasr):
                return kasr.__makhraj
        @makhraj.setter
        def makhraj(kasr,meghdar):
                if meghdar==0:
                        raise ZeroDivisionError("مخرج کسر نمی‌تواند صفر باشد!")
                kasr.__makhraj=meghdar
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
                gCd=kasr.gcd(kasr.__soorat,kasr.__makhraj)
                kasr.__soorat//=gCd
                kasr.__makhraj//=gCd
                return kasr
        def be_adad(kasr):
                return kasr.__soorat/kasr.__makhraj
        @property
        def check_makhraj(kasr):
                if kasr.__makhraj==0:
                        raise ZeroDivisionError("مخرج کسر نمی‌تواند صفر باشد!")

