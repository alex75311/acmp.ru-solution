a = input()
res1 = []
res2 = []
for el in input().split():
    if int(el) % 2 != 0:
        res1.append(el)
    else:
        res2.append(el)
print(' '.join(res1))
print(' '.join(res2))
print("YES") if len(res2) >= len(res1) else print("NO")
