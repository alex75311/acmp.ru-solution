a = int(input())
b = int(input())


def reve(lst, x, y):
    if lst[y] != '0':
        lst[x], lst[y] = lst[y], lst[x]
    else:
        reve(lst, x + 1, y + 1)
    return lst


def max_a(x, rev=False):
    x = str(abs(x))
    lst = []
    result = ''
    for el in x:
        lst.append(el)
    lst.sort(reverse=rev)
    while lst[0] == '0':
        lst = reve(lst, 0, 1)
    result += ''.join(lst)
    return int(result)


if a != 0:
    if a > 0:
        a = max_a(a, True)
    else:
        a = max_a(a, False) * -1

if b != 0:
    if b > 0:
        b = max_a(b, False)
    else:
        b = max_a(b, True) * -1

print(a - b)
