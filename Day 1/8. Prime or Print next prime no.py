# # Factors only available in the half of the range

a=20
count=0
i=2
while(i<=a//2):
    if(a%i==0):
        count+=1
    if(count>1):
        a+=1
        i=1
        count=0
    i+=1
print(a)


#count prime digits in a number
n = 66876
c = 0
while(n):
    if n%10 in [2,3,5,7]:
        c += 1
    n //= 10

print(c)