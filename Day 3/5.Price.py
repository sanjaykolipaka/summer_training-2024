l = list(map(int,input().split(' ')))
maxprice = 0
for i in range(len(l)-1):
    j = i+1
    if l[i] < l[j]:
        i = j
    price = l[j] - l[i]
    maxprice = min(maxprice,price)
print(abs(maxprice))

    


