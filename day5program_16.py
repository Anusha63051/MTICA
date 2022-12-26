def count_Digits(s):
    n_Digit=0
    for i in s:
        if i in '12345678':
            n_Digit+=1
        return n_Digit
str1=input()
a=count_Digits(str1)
print("no of Digits in:'",str1,"' is",a)

