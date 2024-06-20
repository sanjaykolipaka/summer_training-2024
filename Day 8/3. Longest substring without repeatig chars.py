# def longest(s, i,maxi ,length):
#     if i == len(s) -1:
#         return max
#     if s[i] < s[i+1] and s[i] not in s[:i]:
#         length = length 

#         maxi = max(maxi,length)


s = input()
maxi = 0
l = 0
i = 0
# while(i<len(s)):
#     j = i
#     while j < len(s):
#         if s[j] < s[j+1] and s[j] not in s[i:j]:
#             l += 1
#         else:
#             l -= 1
        

i = 0
j=0
while(i < len(s)):
    
    if s[j] < s[j+1] and s[j] not in s[i:j]:
        l += 1
    else:
        while i < j :
            if s[i] == s[j]:
                break
            l -= 1
            i += 1
    j += 1
    maxi = max(l,maxi)
print(maxi)

            
