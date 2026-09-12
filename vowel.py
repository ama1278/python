word=input('enter any word ')
vowels=['a','e','i','u','o','A','I','E','U','O']
count=0
for i in word:
    if i in vowels:
        count+=1
print(count)        
        