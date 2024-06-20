def maxprofit(i, profit, j):
    if j >= len(hrs):
        return profit
    if i <= hrs[j][0]:
        profit =profit + m[j]
        i = hrs[j][1]
    return maxprofit(i,profit,j+1)        
    

hrs = [(1,3), (2,5), (4,6), (6,7), (5,8), (7,9)]
m = [5,6,5,4,11,2]
maxi = 0
c = 0
for i in range(len(hrs)):
    for j in range(i+1,len(hrs)):
        c += 1
        maxi = max(maxi,maxprofit(hrs[i][1],m[i],j))

print("Maximim Profit= " , maxi)
print(c)