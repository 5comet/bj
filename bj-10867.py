n = int(input())
numbers = list(set(map(int, input().split())))
minus = [i for i in numbers if i < 0]
plus = [j for j in numbers if j >= 0]
minus.sort() ;plus.sort()
minus.extend(plus)
print(*minus)