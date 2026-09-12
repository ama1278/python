list1=['red', 'green', 'purple', 'crimson', 'blue', 'blue', 'yellow', 'blue']
item=input('enter any item ')
indexes=[]
count=0
for i in list1:
    if list[i]==item:
        count+=1
        indexes.append(i)
if count>0:
    print(f'there is {count} number of item')   
    print(f'items are in this indexes:{indexes}')        
else:
    print(f'{item} is not here')           