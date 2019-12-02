*l, = map(int, input().split())
x, y = map(int, input().split())

if l[1] == l[3]:
    if y == l[1] or y == l[3]:
        pass
    elif y < l[1]:
        y += (l[1] - y) * 2
    else:
        y -= (y - l[1]) * 2
else:
    if x == l[0] or x == l[2]:
        pass
    elif x < l[0]:
        x += (l[0] - x) * 2
    else:
        x -= (x - l[0]) * 2
print(x, y)
