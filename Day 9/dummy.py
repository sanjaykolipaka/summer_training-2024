# def search(l,i,target,l1):
#     l1 = []
#     if i == len(l):
#         return l1
#     if l[i] == target:
#         l1.append(i)
#     print l1
#     c = search(l,i+1,target,l1)
#     return c


# l = [1,3,6,4,5,6]
# l1 = []
# print(search(l,0,6,l1))


def search(l,i,target):
    l1 = []
    if i == len(l):
        return l1
    if l[i] == target:
        l1.append(i)
    c = search(l,i+1,target)
    print(l1)


l = [1,3,6,4,5,6]
print(search(l,0,6))



