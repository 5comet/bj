n = input()
m = int(n[-1])
i = 1
s = 0
for j in range(12):
    if j % 2 == 0:
        if n[j] == '*':
            i *= 1
        else: s += int(n[j])
    else:
        if n[j] == '*':
            i *= 3
        else: s += int(n[j]) * 3

for k in range(10):
    if m == (10 - (s + i * k) % 10) % 10: print(k)