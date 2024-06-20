# s = "leetc**od*e"
# stack = []
# for i in s:
#     if i == '*':
#         stack.pop()
#     else:
#         stack.append(i)
# print(''.join(stack))


s = "is2 sentence4 This1 a3"
l = s.split(" ")
l1 = [0] * len(l)


for i in l:
    l1[int(i[-1])-1] = i[:-1]

print(" ".join(l1))