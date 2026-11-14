def lis(set):
        if not set:
                return 0
        longest_lis=[0 for i in range(len(set))]
        for i in range(len(set)):
                for j in range(i):
                        if set[j]<set[i]:
                                longest_lis[i]=max(longest_lis[i],longest_lis[j]+1)
        return max(longest_lis)
sett=list(map(int,input('enter numbers').split()))
print(lis(sett))                        