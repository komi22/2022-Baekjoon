# 소수 구하기 (1929)

import sys

n1, n2 = map(int, input().split())

for cnt_i in range(n1, n2+1):
    if (cnt_i == 1): 
        continue
    for cnt_j in range(2, int(cnt_i**0.5)+1):
        if (cnt_i % cnt_j == 0):
            break
    else:
    	print(cnt_i)
