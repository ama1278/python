
def factoriel(n):
        ans=1
        for i in range(1,n+1):
                ans=ans*i
        return ans            
def digit(v):
        were=[]
        for i in range(len(str(v))):
                digits=v%10
                were.append(digits)
                v=v//10
        were.reverse()        
        return were
       
def perm (n):
        a=[]
        r=digit(n)
        for i in range(0,len(n)):
                ld=n//factoriel(len(n)-i-1)
                n-=ld*factoriel(len(n)-i-1)
                a.append(r[ld])
                r.pop(ld)
        return a

if __name__=='__main__':
        abc=[]
        a=int(input('enter number'))
        print(a)
                
       
                       
                