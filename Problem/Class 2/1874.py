# 스택 수열 (1874)

import sys

n = int(input())

nums = [ int(sys.stdin.readline()) for _ in range(n) ]

stack = []
result = []
tmp = 1
no = 0

for num in nums:
    while (tmp <= num):
        stack.append(tmp)
        result.append('+')
        tmp += 1

    if (stack[-1] == num):
        result.append('-')
        stack.pop()
    else:
        no = 1
        break

if (no == 0):
    for _ in result:
        print(_)
else:
    print("NO")
