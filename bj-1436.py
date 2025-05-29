n = int(input())
if n == 1: print(666); exit()
e = 666
cnt = 1
while True:
    e += 1
    if '666' in str(e):
        cnt +=1
        if n == cnt: print(e); break
