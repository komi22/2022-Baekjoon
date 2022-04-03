# 별 찍기 - 2 (2439)

num = int(input())

for cnt_i in range(1, num+1):
    print(" "*(num-cnt_i) + "*"*cnt_i)
