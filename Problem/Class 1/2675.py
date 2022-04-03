# 문자열 반복 (2675)

n = int(input())

for _ in range(n):
    count, string = input().split()
    for alp in string:
        print(alp * int(count), end='')
    print()
