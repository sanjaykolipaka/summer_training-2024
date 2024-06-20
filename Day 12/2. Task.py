def fun(i,j,sum):
    if j > len(l2)-1:
        return l3
    if l2[j]%2 != 0:
        sum = sum + i+l2[j]
        l3.append(sum + i+l2[j])
    return fun(i,j+1,sum)

# def fun1():
#     if k > len(l1)-1:
#         return 
#     if 


l1 = [6,3,2,9,4,2]
l2 = [8,7,5,3,6,9]
l3 = []


for i in l1:
    if i%2 == 0:
        fun(i,0,0)
print(l3)





