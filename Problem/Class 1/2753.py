year=int(input())
if year%400==0:
    print(1)
elif year%100==0 and not year%400==0:
    print(0)
elif not year%4==0:
    print(0)
else:
    print(1)
