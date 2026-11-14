n=list(map(int,input('enter numbers: ').split()))
longest_lis=[1 for i in range(len(n)+1)]
for i in range(len(n)):
        for j in range(i):
                if n[j]<n[i] and longest_lis[j]+1>longest_lis[i]:
                        longest_lis[i]=longest_lis[j]+1
print(f'hamme shahkilid ha :{longest_lis}')
print(max(longest_lis))                        