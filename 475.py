def pr():
    with open('INPUT.TXT', "r", encoding='utf-8') as f:
        s = f.readlines()
        s = list(map(int, ''.join(s).strip().split()))

    s = sorted(s)
    q = set(s)
    x = s[1] - s[0]
    if len(q) != len(s) and len(q) != 1:
        return 'No'
    for i in range(1, len(s)):
        if s[i] - s[i - 1] == x:
            if i == len(s) - 1:
                return 'Yes'
        else:
            return 'No'


print(pr())
