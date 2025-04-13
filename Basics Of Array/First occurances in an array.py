def first_occur(a):
    n = len(a)
    target = int(input("Enter Target Element : "))
    for i in range(n):
        if a[i] == target:
            return i
    return -1
a = [1,2,3,4,5,2]
print("Index :  ",first_occur(a))