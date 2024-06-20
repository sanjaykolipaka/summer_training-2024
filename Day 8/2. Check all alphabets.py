s = "the quick brown fox jumps over thr lazy dog"
d= {}
for i in s:
    if i.isalpha():
        d[i] = 1
    
print(d)
if len(d) == 26:
    print("Yes")
else:
    print("NO")

       