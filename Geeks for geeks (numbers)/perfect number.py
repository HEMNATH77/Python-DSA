#finding the perfect number "n" denotes the limit to find the perfect numbers

n = int(input("Enter the limit  : "))

for num in range(1,n+1):
    sum = 0

    for i in range(1,num):
        if num %i == 0:
            sum +=i

    if sum == num:
        print(num)









