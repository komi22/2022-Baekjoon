n, m = input().split()
n = int(n)
m = int(m)

card_list = list(map(int, input().split()))
s = list()

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if card_list[i] + card_list[j] + card_list[k] <= m:
                s.append(card_list[i] + card_list[j] + card_list[k])

s.sort()

print(s[-1])
