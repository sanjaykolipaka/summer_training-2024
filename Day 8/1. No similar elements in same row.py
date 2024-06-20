l = [2,3,1,3,4,3,2]
d = {}
l2 = []
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1


c = 0
while c!=len(l):
    l1 = []
    for i in d:
        if d[i] != 0:
            l1.append(i)
            d[i] -= 1
            c += 1
    l2.append(l1)

print(l1)

