def validate(n, matrix,s):
    flag = 0
    for i in range(len(s)):
        if s[i] in matrix[i%n]:
            matrix[i%n].remove(s[i])
            flag = 1
        else:
            flag = 0
            break
    if flag == 1:
        print("Yes")
    else:
        print("No")



n = int(input())
matrix = []
print("Enter the entries : ")
for i in range(n):
    a =[]
    for j in range(n):      
         a.append(input())
    matrix.append(a)
s = input()
validate(n, matrix,s)
          
        