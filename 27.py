w, h = map(int, input().split())

max = w * h
res = [0] * w
for i in range(w):
    res[i] = [0] * h


def zap(s):
    *mass, = map(int, s.split())
    for i in range(mass[0], mass[2]):
        for j in range(mass[1], mass[3]):
            if res[i][j] == 1:
                continue
            else:
                res[i][j] = 1


for _ in range(int(input())):
    zap(input())

for i in range(len(res)):
    max -= res[i].count(1)
print(max)
