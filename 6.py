inp = input()
try:
    if inp[0] not in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H') or inp[3] not in ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'):
        print('ERROR')
    elif int(inp[1]) < 1 or int(inp[1]) > 8 or int(inp[4]) < 1 or int(inp[4]) > 8:
        print('ERROR')
    elif inp[2] != '-':
        print('ERROR')
    else:
        x = ord(inp[0]) - ord(inp[3])
        y = int(inp[1]) - int(inp[4])
        if (x == 2 or x == -2) and (y == 1 or y == -1):
            print("YES")
        elif (y == 2 or y == -2) and (x == 1 or x == -1):
            print("YES")
        else:
            print("NO")
except:
    print('ERROR')
