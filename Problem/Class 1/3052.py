# 나머지 (3052)

n_list = []; count = 1

for cnt_i in range(10):
    n = int(input())
    n_list.append(n % 42)

x_list = list(set(n_list))

print(len(x_list))
