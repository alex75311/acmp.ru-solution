a = int(input())
res = 0
while a != 0:
    if a % 2 == 1:
        res += 1
    a = a // 2
print(res)