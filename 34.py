z, a = map(int, input().split())
c = input()

d = [c[x:x+a] for x in range(len(c) - a + 1)]
r = list(set(d))
if len(r) != len(d):
    print('YES')
else:
    print('NO')
