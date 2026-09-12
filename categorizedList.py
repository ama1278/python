#with while
colors = ["red", "green", "purple", "yellow", "crimson", "white", "black", "pink"]
new=[]
start=0
end=len(colors)-1
i=0
while i<4:
    new.append([colors[start],colors[end]])
    i+=1
    start+=1
    end-=1
print(new)    
print('_-'*50)
#with for
colors = ["red", "green", "purple", "yellow", "crimson", "white", "black", "pink"]
new=[]
for i in range(len(colors)//2):
    new.append([colors[i],colors[-(i+1)]])
print(new)    
