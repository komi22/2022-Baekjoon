# 수 찾기 (1920)

import sys

n = int(input())
n_list = sorted(list(map(int, input().split())))
m = int(input())
m_list = list(map(int, input().split()))


for m in m_list:

    check = 0
    start = 0
    end = len(n_list) - 1

    while ( start <= end ):
        
        tmp = ( start + end ) // 2

        if ( m == n_list[tmp]):
            print('1')
            check = 1
            break

        elif ( m > n_list[tmp] ):
            start = tmp + 1
        elif ( m < n_list[tmp] ):
            end = tmp - 1

    if (check == 0):
        print("0")
