input()
a = set(map(int, input().split()))
b = set(map(int, input().split()))
if len(b) < len(a):
    a, b = b, a
c = []
for i in a:
    if i in b:
        c.append(i)

r = ' '.join(map(str, c))
print(r)
