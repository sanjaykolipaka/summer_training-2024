
# def path(i, j, c):
#     if i >= m or j >= n or i < 0 or j < 0 or (i, j) in l1:
#         return c
#     if i == m-1 and j == n-1:
#         l2.append((i,j))
#         print(l2)
#         c = c+1
#         l2.pop()
#         return c
#     l1.append((i, j))
#     l2.append((i,j))
#     if (i+1,j) not in l1:
#         c = path(i+1, j, c) 
#     if (i-1,j) not in l1:
#         c = path(i-1, j, c) 
#     if (i,j+1) not in l1:
#         c = path(i, j+1,c) 
#     if (i,j-1) not in l1:
#         c = path(i, j-1, c)

#     l1.remove((i, j))
#     l2.pop()
#     return c

# m = 4
# n = 3
# l1 = []
# l2 = []

# result = path(0, 0, 0)
# print(result)





def path(i, j, m, n, l1):
    # Base cases: out of bounds or revisit
    if i >= m or j >= n or i < 0 or j < 0 :
        return 0
    # Base case: reached the bottom-right corner
    if i == m-1 and j == n-1:
        return 1
    
    # Explore all possible directions
    paths = (
        path(i+1, j, m, n, l1) +
        path(i, j+1, m, n, l1) 
    )
    
    return paths

m = 12
n = 23
# Use a set for visited cells
visited = set()
# Start from the top-left corner
result = path(0, 0, m, n, visited)
print(result)
