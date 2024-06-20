l = [3, 5, 4, 3, 6, 7, 1, 2, 4, 3, 3, 7, 6, 8 ,8]
d = {}
for i in l:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for i in d:
    print(i, '-', d[i])
