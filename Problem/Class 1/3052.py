# 집합 자료형 이용하여 중복제거 후 길이 출력
import sys

temp = []

for i in range(10):
    a = int(sys.stdin.readline())
    temp.append(a%42)
answer = set(temp)
print(len(answer))