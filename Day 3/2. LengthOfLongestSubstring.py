def Length(s):
    length,maxlen = 1,1
    for i in range(len(s)-1):
        if ord(s[i+1]) == ord(s[i])+1:
            length +=1
        else:
            length = 1
        maxlen = max(length, maxlen)
    return maxlen


s  = input()
print(Length(s))