l = [4,8,8,8,2,8,4]
count = 1
temp = l[0]
for i in range(1, len(l)):
    if l[i] == temp :
        count += 1
    else:
        if count > 1:
            count -= 1
        else:
            temp = l[i]
print(temp)