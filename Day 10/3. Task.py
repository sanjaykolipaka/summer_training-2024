s = "hello:5438,car:214,book:8799,apple:2187"
s = s.split(',')
s1 = ""

for i in s:
    i = i.split(':')
    length = len(i[0])
    flag = 0
    for j in range(len(i[1])):
        if str(length) in i[1]:
            flag = 1   
            break
        length -= 1
    if flag == 1:
        s1 += i[0][length-1]
    else:
        s1 += 'x'
print(s1)


     