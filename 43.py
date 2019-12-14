m = 0
x = input().split('1')

for el in x:
    if m < len(el):
        m = len(el)
print(m)