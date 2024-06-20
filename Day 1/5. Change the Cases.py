# s = 'placements'
# for i in s:
#     if i in 'aeiou':
#         s = s.replace(i, chr(ord(i) - 32))
# print(s)



s = 'placements'
for i in s:
    if i in 'AEIOU':
        s = s.replace(i, chr(ord(i) - 32))
    else:
        s = s.replace(i, chr(ord(i) + 32))
print(s)