def is_prime(n):

    if n < 2:
        return False
    a = (n//2)+1
    for i in range(2, a):
        if n % i == 0:
            return False
    return True

def nth_prime(n):

    num, count = 1, 0
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

# Get user input
N = int(input("Enter N: "))
print(nth_prime(N))
