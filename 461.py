i = int(input())
*q, = sorted(map(int, input().split()))
r = 0
for x in range(i // 2 + 1):
    r += q[x] // 2 + 1
print(r)
