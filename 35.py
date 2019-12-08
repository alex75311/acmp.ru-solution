x = int(input())

for _ in range(x):
    n, m = map(int, input().split())
    print(round(19*m+(n+239)*(n+366)/2))
