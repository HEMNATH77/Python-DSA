def odd_even(a):
    odd = 0
    even = 0
    for i in a:
        if i % 2 ==0:
            even += 1
        else:
            odd += 1
    return odd , even

a = [1,2,3,4,6]
print("Odd , even : ",odd_even(a))