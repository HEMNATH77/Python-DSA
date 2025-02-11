#gcd + lcm
def hcf(a,b):
    if b ==0:
        return a
    return hcf(b,a % b)
def lcm(a,b):
    return a * b // hcf(a,b)
a = int(input("Enter a : "))
b = int(input("Enter b : "))
print("HCF : ",hcf(a,b))
print("LCM : ",lcm(a,b))


