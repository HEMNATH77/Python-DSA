def missing(a):
    n = len(a)
    sum = 0
    for i in range(n):
        sum = sum + a[i]
    m = n + 1
    miss = (sum - m)// 2
    return miss
a = [1,2,3,4,6]
print(missing(a))
