a, b = map(int, input().split())
if a < 0: a *= -1
if b < 0: b *= -1
res = a

while res % a or res % b != 0:
    res += a
print(res)
