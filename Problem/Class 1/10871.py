# X보다 작은 수 (10871)

n, x = map(int, input().split())
n_list = list(map(int, input().split()))
p_list = []

for num in n_list:
    if ( num < x ):
        p_list.append(num)

for num in p_list:
    print(num, end=' ')


