def visit(graph,l,j):
    l.append(j)
    print(j)
    for i in graph[j]:
        if i[0] not in l:
            visit(graph,l,i[0])


def printAllPaths(graph,j,end):
    l.append(j)
    if j == end:
        print(l)
        l.pop()
        return 
    for i in graph[j]:
        if i[0] not in l:
            printAllPaths(graph,i[0],end)

    l.pop()


def printAllPathswithCost(graph,l,j,cost):
    l.append(j)
    if j == 2:
        print(l," cost = ",cost)
        l.pop()
        return
    for i in graph[j]:
        if i[0] not in l:
            cost = cost + i[1]
            printAllPathswithCost(graph,l,i[0],cost)
            cost = cost - i[1]

    l.pop()


def printmincost(graph,j,cost,maxi,l,l1):
    l.append(j)
    if j == 2:
        if (cost < maxi):
            maxi = cost
            l1 = l.copy()
        l.pop()
        return maxi, l1
    for i in graph[j]:
        if i[0] not in l:
            maxi, l1 = printmincost(graph,i[0],cost + i[1],maxi,l,l1)

    l.pop()
    return maxi, l1






  
graph ={5:[[7,10],[3,30]], 7:[[5,10],[4,20],[3,50]], 4:[[7,20],[8,60],[2,70]], 2:[[4,70],[8,80]], 8:[[4,60],[2,80],[3,40]], 3:[[5,30],[7,50],[8,40]]}
l = []
l1 = []
visit(graph,[],5)
# printAllPaths(graph,5, 2)
# printAllPathswithCost(graph,[],5,0)
# print(printmincost(graph,5,0,999999,[],[]))



# for k in graph:
#     if k != 5:
#         printAllPaths(graph,5,k)







