def move_zero(a):
    n = len(a)
    pos = 0
    for i in range(n):
        if a[i] != 0:
            a[pos] = a[i]
            pos += 1
    while pos < n :
        a[pos] = 0
        pos += 1
    return a
a = [1,3,0,2,0,4]
print(move_zero(a))