l = [2,6,2,3,10,7,1,0,5,7]
l2 = l.copy()
l3 = l.copy()
i = 0
j = 1
count = 0
while j < len(l):
    if l[i] > l[j]:
        count += (l[i] - l[j])
        j += 1
    else:
        i = j
        j = i+1
print(count)





