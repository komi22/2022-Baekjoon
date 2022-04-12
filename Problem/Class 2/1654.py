# 랜선 자르기 (1654)

import sys

k, n = map(int, input().split())


'''
line_list = []
for cnt_i in range(k):
    line_list.append(int(input()))

시간 초과를 고려하여 위보다 더 효율 적인 아래 방법으로 반복적인 입력 값을 받을 수 있음
'''

lines = [ int(sys.stdin.readline()) for _ in range(k) ]


# 랜선의 길이는 2^31-1보다 작거나 같은 자연수이다 => 브루트 포스로는 풀이 불가 (시간초과)
# 이분 탐색으로 풀이 
# 항상 정수길이 만큼 자르고, 남는 랜선은 버려야한다 -> // 연산자 사용

min_len = 1
max_len = max(lines)

while (min_len <= max_len): # 최대 길이를 찾기 위한 범위를 반복문의 조건으로 잡아줌
                            # 범위가 한 점으로 같아지는 순간이 정답
    count = 0
    tmp = (min_len + max_len) // 2

    for line in lines:
        count += line // tmp
    
    if (count < n): 
        max_len = tmp - 1 
    elif (count >= n): # 같은 경우를 고려하는 이유는 같은 조건인데 값이 더 큰 경우도 있으므로
        min_len = tmp + 1 

print(max_len)

