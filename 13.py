x, y = input().split()
k = 0
b = 0
for idx, el in enumerate(x):
    if x[idx] == y[idx]:
        b += 1
    elif x[idx] in y:
        k += 1
print(b, k)
