P = int(input("Enter principle amount : "))
T = int(input("Enter no.of Years : "))
R = int(input("Enter Rate of interest : "))

Amount = P*((1+R/100))**T

CI = Amount - P

print("Compound Interest : ",CI)



