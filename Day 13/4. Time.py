# n = 100000
# print(n//3600,"hr :", (n%3600)//60,"m : ", ((n%600)%60),"s")

# m = 65476
# print(m//600,"year  ",(m%600)//30, "months", (n%) )


def search(i,j):
    for j in range(len(matrix[0])):
        if matrix[i][j] == target:
            return "true"
    return "false"



matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13
for i in range(len(matrix)):
    
    if target >= matrix[i][0] and target < matrix[i+1][0]:
        # print(matrix[i][0])
        # print(matrix[i+1][0])
        print(search(i,0))
        break
