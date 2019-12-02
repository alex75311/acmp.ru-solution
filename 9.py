input()
a = input().split()
min = int(a[0])
max = int(a[0])
min_id = 0
max_id = 0
proiz = 1
summ = 0
for idx, el in enumerate(a):
    if max < int(el):
        max = int(el)
        max_id = idx
    if min > int(el):
        min = int(el)
        min_id = idx
if min_id < max_id:
    for el in range(min_id + 1, max_id):
        proiz *= int(a[el])
else:
    for el in range(max_id + 1, min_id):
        proiz *= int(a[el])
for el in a:
    if int(el) > 0:
        summ += int(el)

print(summ, proiz)
