s = "school"
l  = ['l',2,'r', 3,'l',1]
temp = ""
for i in range(0,len(l),2):
    if l[i] == 'l':
        temp += s[l[i+1]]
    else:
        temp += s[-(l[i+1]-1)]

# if temp in s:
#     print("Yes")
# else:
#     print("No")


i = 0
while i < len(s)-(len(temp)-1):
    print(s[i:len(temp)])
    if sorted(s[i:i+len(temp)])== sorted(temp):
        print("Yes")
        break
    i +=1 
print("No")