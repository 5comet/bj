def tri(x):
    tr = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    tr.extend(tr[i + 7] + tr[i + 8] for i in range(x))
    return tr[x-1]
t = int(input())
ans = [str(tri(int(input()))) for _ in range(t)]
print('\n'.join(ans))
