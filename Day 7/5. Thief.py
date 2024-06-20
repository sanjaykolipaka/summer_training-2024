


def Thief(l):
    if len(l)==0:
        return 0
    if len(l) == 1:
        return l[0]
    if len(l) == 2:
        return max(l)
    
    le = l[0] + Thief(l[2:])
    re = l[0] + Thief(l[3:])
    return max(le,re)

l = list(map(int,input().split(" ")))
print(Thief(l))