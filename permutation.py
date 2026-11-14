


def factoriel(n):
        ans=1
        for i in range(1,n+1):
                ans=ans*i
        return ans            

def perm (x,n):
        a=[]
        r=[i for i in range(1,n+1)]
        for i in range(0,n):
                ld=x//factoriel(n-i-1)
                x-=ld*factoriel(n-i-1)
                a.append(r[ld])
                r.pop(ld)
        return a

if __name__=='__main__':
        a=int(input('enter number'))
        for i in range(0,factoriel(a)):
                print(perm(i,a))
                        
                

        
        