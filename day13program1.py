##lst=['apple','gua','mango']
##res_lst=list(map(len,lst))
##print(res_lst)
##
##inp=input()
##temp=inp.split()
##ans=[len(i) for i in temp]
##print(*ans)


def solveProblem(s):
    lst=s.split()
    return [len(i)for i in lst]
inp=input()
print(*solveProblem(inp))
