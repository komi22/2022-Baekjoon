# A+B - 3 (10950)

c = int(input())
n_list = []

for cnt_i in range(c):
    n1, n2 = map(int, input().split())
    n_list.append(n1+n2)

for num in n_list:
    print(num)
