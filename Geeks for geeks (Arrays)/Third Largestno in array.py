n = [9,8,7,6,4]

a = len(n)

largest = -1
second = -1
third = -1

for i in range(a):
    if n[i] > largest:
        largest = n[i]
for i in range(a):
    if n[i] > second and n[i] !=largest:
        second = n[i]
for i in range(a):
    if n[i] > third and n[i] != largest and n[i] != second:
        third = n[i]

print("Third Largest : ",third)




