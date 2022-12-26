def extract_Consonant(s):
    Consonant=0
    for i in s:
        if i in 'wrtyplkh':
            Consonant+=1
        return Consonant
str1=input()
a=extract_Consonant(str1)
print("no of Consonant in:'",str1,"' is",a)

