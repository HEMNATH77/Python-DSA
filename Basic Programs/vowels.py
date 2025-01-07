def vowel_count(str):
    count = 0

    vowel = "aeiouAEIOU"

    for i in str:
        if i in vowel:
            count = count + 1
    print("No of Vowels :",count)

str = " I am Batman"
vowel_count(str)


#n = "I am Batman"

#vowels ="aeiouAEIOU"

#c  ={ i : n.count(i) for i in vowels if i in n}
#print(c)






