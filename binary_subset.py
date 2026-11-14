def binary(x,y):
        binary_list=[]
        for i in range(1,y + 1):
                binary_list.append(x%2)
                x=x//2
        binary_list.reverse()        
        return binary_list





n=int(input("enter ur number: "))
a= [i for i in range( 1, n+1)]
for i in range(0,2**n):
        k=binary(i,n)
        ans=[]
        for j in range(0,n):
                if k[j]==1:
                        ans.append(a[j])
        print(ans)                        
                        
        