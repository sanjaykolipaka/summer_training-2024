# R = int(input("Enter the number of Rows and columns:"))
# matrix = []
# print("Enter the entries rowwise:")
# for i in range(R):
#     a =[]
#     for j in range(R): 
#          a.append(int(input()))
#     matrix.append(a)
 
# for i in range(R):
#     for j in range(C):
#         print(matrix[i][j], end = " ")
#     print()






def fire(a, i,j):
    if i < 0 or j < 0 or i > len(a)-1 or j > len(a)-1:
        return 
    if a[i][j]!=1:
        return
    if  a[i][j] == 1:
        a[i][j] = 2
    fire(a,i-1,j)
    fire(a,i+1,j)
    fire(a,i,j-1)
    fire(a,i,j+1)
    return a

a=[[0,1,1,1,0,1],
   [0,1,0,1,0,0],
   [1,0,1,1,0,0],
   [0,0,0,1,1,1],
   [1,1,0,0,0,1],
   [1,1,1,0,1,0]]
i = 4
j = 5

fire(a,i-1,j-1)


for i in range(6):
    for j in range(6):
        print(a[i][j], end = " ")
    print()

