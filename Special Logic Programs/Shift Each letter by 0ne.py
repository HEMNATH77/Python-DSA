def shift_letter(a):
    n = len(a)
    alpha = "abcdefghijklmnopqrstuvwxyz"
    result = ""
    for i in a:
        index = alpha.index(i)
        result += alpha[index - 1]
    return result
a = "zav"
print(shift_letter(a))
