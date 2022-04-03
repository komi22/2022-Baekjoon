# 알파벳 찾기 (10809)

word = list(input())
alp_list = []

lens = len(word)

for cnt_i in range(0, 26):
    alp_list.append(chr(ord('a') + cnt_i))

for cnt_i in range(0, 26):

    alp = alp_list[cnt_i]

    if (alp in word): 
        idx = word.index(alp)
        alp_list[cnt_i] = idx
    else:
        alp_list[cnt_i] = -1

for num in alp_list:
    print(num, end=' ')
