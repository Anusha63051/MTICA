def count_Consonants(s):
    Consonants=0
    for i in s:
        if i in 'wrtyplkh':
            Consonants+=1
        return Consonants
str1=input()
a=count_Consonants(str1)
print("no of Consonants in:'",str1,"' is",a)

