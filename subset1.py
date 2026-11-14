n=int(input('enter ur number '))
sets=list(range(1,n+1))
subsett=[[]]
for subset in sets:
        subs=[]
        for subb in subsett:
                subs.append(subb+[subset])
        subsett=subsett+subs
subsett=sorted(subsett,key=len)
print(subsett)                