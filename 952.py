n, m = map(int, input().split())

if m == 0:
    print(n, n)
elif n == 0:
    print('Impossible')
else:
    mx = n + m - 1
    if m - n < 0:
        print(n, mx)
    else:
        mn = n + (m - n)
        print(mn, mx)
