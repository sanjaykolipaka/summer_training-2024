# def even_odd(x,s,e):
#     if(x==len(a)):
#         return (s,e)
#     if(a[x]%2==0):
#         s+=a[x]
#     if(b[x]%2!=0):
#         e+=b[x]
#     return even_odd(x+1,s,e)



# a=[3,8,5,4,3]
# b=[5,0,9,3,2]
# print(even_odd(0,0,0))



def even(x):
    if x == 0:
        return 0
    return x + even(x-2)


x = 10
print(even(x))
