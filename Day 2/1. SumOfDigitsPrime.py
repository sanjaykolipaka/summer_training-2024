def sum_of_digits(number):
    total = 0
    if number<10:
        return number
    while number >=10 :
        total = 0
        while number > 0:
            total += number % 10
            number //= 10
        number = total
    return total


number = int(input('Enter a Number :'))
temp = sum_of_digits(number)
k=number
while True:
    if temp in [1, 2, 3, 5, 7]:
        print(k)
        break
    else:
        k=number+1
        temp=sum_of_digits(k)
   









