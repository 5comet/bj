string = list(input())
string2 = ''

for s in string:
    s = ord(s)
    s -= 3
    if s < 65 : s += 26
    if s > 90 : s -= 155
    string2 += chr(s)
    
print(''.join(string2))
