# def reverse(n,rev):
#     if n == 0:
#         return rev
#     rev = rev*10 + n%10
#     return reverse(n//10,rev)


# n = 564725455621
# p = reverse(n,0)

# while True:
#     if n == p:
#         print(n)
#         break
#     else:
#         n = n + 1
#         p = reverse(n,0)


n = 564725455621
s = str(n)
l = len(str(n))
print(s[0:l//2])
print(s[l//2+1:])
if l % 2 == 0:
    if int(s[0:l//2])  >  int(s[(l//2)+1:]):
        print(s[0:l//2] + s[0:l//2][::-1])
    else:
        print(str(int(s[0:l//2])+1) + s[0:l//2][::-1])

else:

    if int(s[0:l//2]) < int(s[(l//2)+1:]):
        print(s[0:l//2]+ str(int(s[l//2])+1) + s[0:l//2][::-1] )
    else:
        print(s[0:l//2]+ s[l//2] + s[0:l//2][::-1])
