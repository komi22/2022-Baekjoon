# 문자열 반복
import sys

t = int(sys.stdin.readline())

temp = [list(map(str,sys.stdin.readline().split())) for _ in range(t)]

for i in temp:
    temp2 = ''
    for z in i[1]:
        temp2 += z*int(i[0])
    print(temp2)