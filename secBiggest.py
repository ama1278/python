numbers = [12, 45, 7 ,89 ,34, 67, 23]
biggest=0
second_biggest=0
for i in numbers:
    if i>biggest:
        second_biggest=biggest
        biggest=i
    elif i>second_biggest:
        second_biggest=i
print(second_biggest)                