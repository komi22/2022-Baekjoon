# 상수 (2908)

n1, n2 = map(int, input().split())

tmp1 = int(str(n1)[::-1])
tmp2 = int(str(n2)[::-1])

if (tmp1 > tmp2):
    print(tmp1)
else:
    print(tmp2)
