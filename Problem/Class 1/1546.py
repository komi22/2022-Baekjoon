N = int(input())
a = list(map(int, input().split()))
M = max(a)

for q in range(N):
    a[q] = a[q]/M*100

print(sum(a)/N)
