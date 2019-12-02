from out import out

*e, = map(int, input().split())
r = []
for i in range(-100, 101):
    if e[0] * (i ** 3) + e[1] * (i ** 2) + e[2] * i + e[3] == 0:
        r.append(i)

print(out(r))
