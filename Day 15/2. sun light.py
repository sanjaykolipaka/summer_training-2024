l1 = [3, 5, 9 , 6, 8 , 10]
l2 = [3, 5, 9 , 6, 8 , 10]

for i in range(len(l1)-2):
    if l1[i] < l1[i+1]:
        continue
    else:
        l1[i+1] = l1[i]
print("Morning = ",len(set(l1)))

i = len(l2)-1
while i > 0:
    if l2[i] < l2[i-1]:
        continue
    else:
        l2[i-1] = l2[i]
    i -= 1

print("Evening = ",len(set(l2)))
