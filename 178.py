from collections import Counter

input()
a = input()


def qqq(a: str):
    *a, = map(int, a.split())

    q = tuple(set(a))
    m = 0
    if len(a) == 1:
        return ''.join(map(str, a))
    if len(q) == len(a):
        b = min(q)
        r = [x for x in a if x != b]
        r = ' '.join(map(str, r))
        r += ''.join((' ' + str(b)))
        return r
    else:
        c = Counter(a).most_common(len(a))
        if len(c) == 1:
            return ' '.join(map(str, a))
        c.sort(key=lambda i: i[1])
        b = c[-1][0]
        for i in range(len(c) - 1, -1, -1):
            if m == c[i][1]:
                b = min(b, c[i][0])
                m = c[i][1]
            elif m > c[i][1]:
                break
            else:
                m = c[i][1]
                b = c[i][0]
        r = [x for x in a if x != b]
        r = ' '.join(map(str, r))
        r += (''.join((' ' + str(b)) * m))
        return r


print(qqq(a))