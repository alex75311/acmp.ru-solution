input()
s = input()


def my_sort(x: str):
    return ' '.join(map(str, (sorted(list(map(int, x.split()))))))


print(my_sort(s))