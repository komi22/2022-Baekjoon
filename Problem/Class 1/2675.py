t = int(input())
for w in range(t):
    
    r, s = input().split()
    r = int(r)
    for q in s:
     print(q*r, end='')
    print("")
