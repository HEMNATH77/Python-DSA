def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a % b)
a = int(input("Enter a : "))
b = int(input("Enter b : "))
print(gcd(a,b))
