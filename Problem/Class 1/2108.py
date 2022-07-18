import sys

n = int(sys.stdin.readline())

s = list()
for i in range(n):
    s.append(int(sys.stdin.readline()))

total = sum(s)
mean = round(total / n)
print(int(mean))

s.sort()
print(s[int(n/2)])


count = [0]*8002
m = 0
for i in range(n):
    count[s[i]+4000] = count[s[i]+4000] + 1
if n == 1:
    print(s[0])
else:
    m = max(count)
    mode = set()
    for i in range(8002):
        if count[i] == m:
            mode.add(i-4000)

    mode2 = list(mode)
    mode2.sort()
    if len(mode2) == 1:
        print(mode2[0])
    else:
        print(mode2[1])
            

r = s[-1] - s[0]
print(r)



# 슬프다
