a = list(map(int, input().split()))

q = 0 
for z in a:
    q += z**2

print(q % 10)
