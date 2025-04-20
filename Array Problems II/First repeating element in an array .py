def repeating_element(a):
    n = len(a)
    s = []
    min = n
    repeat = -1
    for i in range(n - 1, -1 ,-1):
        if a[i] in s:
            min = i
            repeat = a[i]
        else:
            s.append(a[i])
    return repeat
a = [1,2,3,5,1,6,5]
print(repeating_element(a))