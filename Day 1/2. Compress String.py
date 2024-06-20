# i/p = "aaaabbbcccd"
# o/p = "a4b3c3d1"


s = "aaabbbcccb"
s1 = ""
count = 1
for i in range(len(s)-1):
    if s[i] == s[i+1]:
        count += 1
    else:
        s1= s1 + s[i]+str(count)
        count = 1
s1 = s1 + s[-1] + str(count)
print(s1)



