input()
*a, = map(int, input().split())
q = set(a)
m = 0
b = 0
for i, x in enumerate(q):
    if m < a.count(x):
        m = a.count(x)
        b = x
    elif m == a.count(x):
        b = min(b, x)
r = [x for x in a if x != b]
r = ' '.join(map(str, r))
r += ''.join((' ' + str(b)) * m)
print(r)
