# 벌집을 둘러싼 벌집들이 6의 배수로 증가하는것을 이용
import sys

n = int(sys.stdin.readline())

answer = 1 # 벌집의 개수
count = 1

while n > answer:
    answer += 6 * count
    count+=1
print(count)