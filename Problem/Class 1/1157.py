# 단어 공부 (1157)
# input 함수, upper 함수, set 함수, list 함수, count 함수, max 함수, index 함수

string = input().upper()

alp_list = list(set(string))
count_list = []

for alp in alp_list:
    count_list.append(string.count(alp))

if ( count_list.count(max(count_list)) > 1 ):
    print('?')
else:
    tmp = count_list.index(max(count_list))
    print(alp_list[tmp])
