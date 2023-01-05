##inpl=['papaya','coconut','graps','banana']
##def rev_str(a):
##    return a[::-1]
##outl=list(map(rev_str,inpl))
##print(inpl)
##print(outl)




def reverseString(s):
    ans=[i[::-1] for i in s]
    return ans
inp=input().split()
#print(inp)
print(*reverseString(inp))
