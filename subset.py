def subset(list1):
        if not list1:
                return [[]]
        subbs=subset(list1[1:])     
        return subbs+[[list1[0]]+ sub for sub in subbs]

n=int(input('enter the number '))
for s in subset(list(range(1,n+1))):
        print("{"+','.join(map(str,s))+"}")