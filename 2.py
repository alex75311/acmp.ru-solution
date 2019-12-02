n = int(input())
a = []
if n < 0:
    for i in range(n, -1):
        a.append(i)
    print(sum(a))
elif n == 0:
    print(1)
elif n > 0:
    for i in range(1, n + 1):
        a.append(i)
    print(sum(a))