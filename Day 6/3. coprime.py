def coprime(num1, num2):
    # l = [] 
    # maxnum = max(num1,num2)
    # minnum = min(num1,num2)
    # for i in range(1,maxnum//2):
    #     rem = maxnum % i
    #     if rem == 0:
    #         l.append(i)

    # for i in range(2, minnum // 2):
    #     rem = minnum % i
    #     if rem in l:
    #         return "Not co-primes"
    # return "Co-primes"

    for i in range(2,(min(num1,num2)//2)+1):
        if (num1%i == 0 ) and (num2%i == 0):
            print("Not Prime")
            break
    else:
        print("Coprime")
            





num1 = int(input("Enter Number1"))
num2 = int(input("Enter Number2"))
print(coprime(num1, num2))
