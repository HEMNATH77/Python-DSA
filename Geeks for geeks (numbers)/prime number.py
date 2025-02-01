n = int(input("Enter n : "))

if n > 1:
    a = (n // 2) + 1

    for i in range(2 , a):
        if (n % i) == 0:
            print(" not a Prime number")
            break
        else:
            print("Prime number")
else :
    print("Enter a valid number")







