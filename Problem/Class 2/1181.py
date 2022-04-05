# 단어 정렬 (1181)

n = int(input())

word_list = []
result_list = []

for cnt_i in range(n):
    word_list.append(input())

word_list = list(set(word_list))

for word in (word_list):
    result_list.append((len(word), (word)))

final = sorted(result_list)

for length, word in final:
    print(word)
