def insertion(a):
    for i in range(1,len(a)):
        for j in range(i,0,-1):
            if a[j] < a[j-1]:
                a[j],a[j-1] = a[j-1],a[j]
            else:
                break
    return a

a = [2,4,1,3,5,0]
print(insertion(a))
