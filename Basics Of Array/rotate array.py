def rotate(a,k):
    n = len(a)
    k = k % n
    return a[-k:]+a[:-k]
a = [1,2,3,4,5]
k = int(input("Enter no.of position to rotate : "))
print(rotate(a,k))