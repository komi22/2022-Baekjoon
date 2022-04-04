q = int(input())

if (q % 4 == 0) and (q % 100 != 0) or (q % 400 == 0):
    print(1)
else:
    print(0)
