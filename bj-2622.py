from itertools import combinations
n = int(input())
#밑변 최대 길이는 3으로 나눈 몫까지

if n == 1 or n % 3 != 0 and (n-1) % 2 != 0 : print(0)
else:
    ans = []
    for i in range(1,n//3):
        a = list(combinations(,2))
        
       # ans.extend(a if sum(a) == (n-i) else [])
        print(a)
    # i = 1부터 i == n//3까지 조건 나눠서 계산
    