s = input()
c = 0
for x in range(len(s)-4):
    if s[x:x+5] == '>>-->' or s[x:x+5] == '<--<<':
        c += 1
print(c)
