mat_a = [[1,2,3],[1,2,3],[1,2,3]]
mat_b = [[3,2,1],[3,2,1],[3,2,1]]

def Mul_matrix(a,b):
    result = []
    for i in range(len(a)):
        result.append([])
        for j in range(len(a[0])):
            result[i].append(a[i][j] * b[i][j])      #put this code by altering the arithemetic symbols to get other o/p of operators
    return result
Mul_matrix = Mul_matrix(mat_a,mat_b)
print(" ")
for  r in Mul_matrix:
    print(r)



#import numpy as np
#a = np.array([[1,2,3],[1,2,3],[1,2,3]])
#b = np.array([[1,2,3],[1,2,3],[1,2,3]])
#c = np.add(a,b)
#print(c)