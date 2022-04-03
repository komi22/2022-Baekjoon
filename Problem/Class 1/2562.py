# 최댓값 (2562)

import sys

num_list = []

for cnt_i in range(1, 10):
    num = int(sys.stdin.readline().strip())
    num_list.append(num)

print(max(num_list))
print(num_list.index(max(num_list))+1)
