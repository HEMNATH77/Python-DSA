def reverse_by_d(a):
    n = len(a)
    index = int(input("enter index value : "))
    d = a[index]
    first = []
    for i in range(d,-1,-1):
        first.append(a[i])
    last = []
    for i in range(n - 1,d,-1):
        last.append(a[i])
    final = first + last
    return final

a = [1,7,9,3,2,8,5,6]
print(reverse_by_d(a))