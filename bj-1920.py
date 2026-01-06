import sys
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
numbers = sorted(list(map(int, input().split())))


def bs(list, num):
    find = 0
    start = 0
    end = len(list) - 1
    while start <= end:
        idx = int((start + end) / 2)
        if list[idx] > num:
            end = idx - 1
        elif list[idx] < num:
            start = idx + 1
        elif list[idx] == num:
            find = 1
            break

    return find

m = int(input())
t = list(map(int, input().split()))
for i in t:
    print(str(bs(numbers, i)) + '\n')