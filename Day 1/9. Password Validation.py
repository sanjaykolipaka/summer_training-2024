def Pass_validation(s):
    d={'u':0, 'l':0, 'n':0, 's':0}
    count = 0
    for i in s:
        if(i.islower()):
            d['l']+=1
        elif(i.isupper()):
            d['u'] += 1
        elif(i.isnumeric()):
            d['n']+=1
        else:
            d['s']+=1
    for i in d:
        if d[i] == 0:
            count += 1
    if count == 0:
        print(-1)
    else:
        print(count)

s = input()
if len(s) < 5:
    print(8-len(s))
else:
    Pass_validation(s)