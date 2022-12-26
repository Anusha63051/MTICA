def count_vowel(s):
    n_vowel=0
    for i in s:
        if i in 'AEIOUaeiou':
            n_vowel+=2
        return n_vowel
str1=input()
a=count_vowel(str1)
print("no of vowels in:'",str1,"' is",a)
