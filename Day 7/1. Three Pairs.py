
# for i in range(len(l)-2):
#     for j in range(i+1,len(l)-1):
#         for k in range(j+1,len(l)):
#             print(l[i],l[j],l[k])



def Three_pairs(l,i,j,k):
    if i == len(l) - 2:
        return
    
    # print(l[i],l[j],l[k])
    # Three_pairs(l,i,j,k+1)
    for k in range(j+1, len(l)):
        print(l[i],l[j],l[k])

    if k == len(l)-1:
        i += 1
        
        j = i + 1
        k = j + 1
        return Three_pairs(l,i,j,k)


l = list(map(int,input().split(" ")))
Three_pairs(l,0,1,2)

    
    