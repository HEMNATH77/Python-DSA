def rotate(n,k):
    s = str(n)
    k = k % len(s)
    return int(s[-k:]+s[:-k])
n = int(input("Enter a n : "))
k = int(input("Enter a k : "))
print(rotate(n,k))
