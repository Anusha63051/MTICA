def extract_specialCharacters(s):
   specialCharacters=0
   for i in s:
       if i in '#$%^&*':
           specialCharacters+=1
   return specialCharacters
str1=input()
a=extract_specialCharacters(str1)
print("no of specialCharacters  in:'",str1,"' is",a)

