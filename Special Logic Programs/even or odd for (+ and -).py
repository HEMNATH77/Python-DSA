n = input("Enter a number : ")
a = 0

if n[0] == '-':
    sign = -1
    n = n[1:]
else:
    sign = 1

digits = { '0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}

for d in n:
    a = a * 10 + digits[d]

a = a * sign


if (a%2)==0:
    print("Even")
else:
    print("Odd")



