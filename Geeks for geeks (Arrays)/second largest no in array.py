n =[1,2,3,4,5]

a = len(n)
largest = -1
second_largest = -1


for i in range(a):
    if n[i]> largest :
        largest = n[i]
for i in range(a):
    if  n[i]> second_largest and n[i] != largest:
        second_largest = n[i]

print("Second Largest : ",second_largest)







