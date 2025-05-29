def Fizzbuzz(lis):
    aIndex = 0
    a = 0
    for i in lis:
        if i.isdecimal():
            aIndex = (3 - lis.index(i))
            if aIndex < 0 : aIndex*= -1
            a = int(i) + aIndex
    if a % 3 == 0 and a % 5 == 0:
        return 'FizzBuzz'
    elif  a % 3 == 0 and a % 5 != 0:
        return 'Fizz'
    elif a % 3 != 0 and a % 5 == 0:
        return 'Buzz'
    elif a % 3 != 0 and a % 5 != 0:
        return a    

x = []
for _ in range(3):
    x.append(input())
print(Fizzbuzz(x))