n = int(input())


def faktorial(x):
    if x == 0:
        return 1
    else:
        return x * faktorial(x - 1)


print(faktorial(n))
