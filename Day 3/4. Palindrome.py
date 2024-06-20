def reverse(n,rev):
    if n == 0:
        return rev
    rem = n % 10 
    rev= rev*10 + rem
    return rev(n//10, rev)




n = int(input("Enter a Number"))
rev = 0

if n == reverse(n, rev):
    print("Palindrome")
else:
    print("Not Palindrome")
