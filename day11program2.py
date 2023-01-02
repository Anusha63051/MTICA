def findFrequency(s):
    frequencyDict=dict()
    for i in s:
        if i in frequencyDict:
            frequencyDict[i] =+1
        else:
            frequencyDict[i]=1
    return frequencyDict

n=int(input())
for i in range(n):
    inpStr=input()
    print(findFrequency(inpStr))
