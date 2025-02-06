def p4(n):
    return n > 0 and (n&(n-1)) == 0  and (n-1)% 3 == 0
n = int(input("Enter the number : "))
print(p4(n))