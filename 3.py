print(int(input())**2)
#
# #=============================================
#
a = input()
if int(a) > 9:
    b = str(int(a[:-1]) * (int(a[:-1]) + 1)) + '25'
else: b = 25
print(b)