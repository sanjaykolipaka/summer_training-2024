def backingletters(s, k):
    s1 = ""
    if k > 26:
        k = k%26
    for i in s:
        if i >= 'a' and i <= 'z':
            c = ord(i)-k
            if chr(c) < 'a':
                c += 26
                print(s1.join(chr(c)),end = '')
            else:
                print(s1.join(chr(c)),end = '')
        
    return s1 

s = input("Enter a String : ")
k = int(input("Enter a Key : "))

print(backingletters(s, k))
    


