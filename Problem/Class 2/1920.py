# 이분 탐색의 시간 복잡도는 O(logN)
# Set과 Dictionary의 in연산을 통한 포함 여부 확인의 시간 복잡도는 O(1)

# n이 10만, m도 10만
# 시도한것들 2중 for문, try.Catch문

from time import time
from sys import stdin, stdout

start = time()
n = int(stdin.readline())
nArray = list(map(int, stdin.readline().split()))
nSet = set(nArray)

m = int(stdin.readline())
mArray = list(map(int, stdin.readline().split()))

for i in mArray:
    stdout.write('1\n') if i in nSet else stdout.write('0\n')
end = time()

print(f'시간: {end-start}')
