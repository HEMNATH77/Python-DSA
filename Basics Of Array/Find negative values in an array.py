def negative(a):
    negative_arr = []
    negative_count = 0
    for i in a:
        if i < 0:
            negative_count += 1
            negative_arr.append(i)
    return negative_count,negative_arr

a = [1,2,3,-7,-8,-4,-6]
print("negative_count ,negative_array : ",negative(a))