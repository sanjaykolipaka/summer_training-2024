
def island(i,j,co):
    if i<0 or j< 0 or i >= n or j >=  n or a[i][j]!= 1:
        return co
    if a[i][j] == 1:
        a[i][j] = 2
        co += 1
    co = island(i-1,j,co)
    co = island(i+1,j,co)
    co = island(i,j-1,co)
    co = island(i,j+1,co)
    return co


a=[[0,1,0,0,1], 
   [1,0,0,1,1],
   [0,0,0,0,0], 
   [1,0,0,0,0], 
   [1,0,0,0,1]]
n = 5
m = 0
count = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            k = island(i,j,0)
            m = max(m,k)
            count += 1
print(count)
print(m)
