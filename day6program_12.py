inp=input()

ans=[]
for i in inp:
   if i in '12345678':
        ans.append(i)
print(*ans)

ans=[i for i in inp  if i in '12345678'] 
print(ans)

