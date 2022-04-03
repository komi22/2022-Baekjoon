# 숫자의 개수 (2577)

mul = 1

for cnt_i in range(3):
    num = int(input())
    mul *= num

num_list = list(str(mul))

for cnt_i in range(0, 10):
    print(num_list.count(str(cnt_i)))
