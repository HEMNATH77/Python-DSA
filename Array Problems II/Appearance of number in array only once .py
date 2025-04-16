def single_occurance(a):
    result = 0
    for i in a:
        result ^= i
    return result
a = [2,3,4,3,5,4,5,2,7]
print(single_occurance(a))