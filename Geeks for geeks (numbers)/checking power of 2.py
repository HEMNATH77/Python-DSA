def p2(n):
    return n > 0 and (n&(n-1)) == 0
n = int(input("Enter a number : "))
print(p2(n))