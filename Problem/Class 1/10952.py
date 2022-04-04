# A+B - 5 (10952)

while True:
    try:
        n1, n2 = map(int, input().split())
    except:
        break
    if ( (n1+n2) != 0 ):
        print(n1+n2)
    else:
        break
