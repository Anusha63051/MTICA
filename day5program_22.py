def remove_duplicate(s):
    str2=''
    for i in s:
        if i not in str2:
            str2 +=i
    return str2

str1=input("Enter your text:")
print("without duplicate: ",remove_duplicate(str1)) 
