        #Optimised code

def Find_Duplicates(a):
    new = set()
    repeated = set()
    for i in a:
        if i in new:
                repeated.add(i)
        else:
            new.add(i)
    return list(repeated)

a = [1,2,3,1,3,4,5]
print(Find_Duplicates(a))

              # OR

#def find_duplicates(a):
#   new = []
#    repeated = []
#       if i in new:
#            if i not in repeated:
#               repeated.append(i)
#       else:
#            new.append(i)
#    return repeated
#
#a = [1,2,3,1,3,4,5]
#print(find_duplicates(a))




