n = int(input())
a = 0
b = 1
c = b
count = 1
while count <= n:
    print(a , end = " ")
    count += 1
    a,b = b,c
    c = a+b
    print()