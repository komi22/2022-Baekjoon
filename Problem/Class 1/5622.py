# 풀이를 보니까 리스트에 알파벳을 넣어놓고 chr()로 바꿔도 되고
# 이중for문으로 입력문자와 리스트안에 알파벳과 
# 비교후 리스트.index(i)+3 으로 했다.

import sys
a = sys.stdin.readline().rstrip()

temp = 0
for i in a:
    if ord(i) >= 65 and ord(i) <= 67:
        temp += 3
    elif ord(i) >= 68 and ord(i) <= 70:
        temp += 4
    elif ord(i) >= 71 and ord(i) <= 73:
        temp += 5
    elif ord(i) >= 74 and ord(i) <= 76:
        temp += 6
    elif ord(i) >= 77 and ord(i) <= 79:
        temp += 7
    elif ord(i) >= 80 and ord(i) <= 83:
        temp += 8
    elif ord(i) >= 84 and ord(i) <= 86:
        temp += 9
    elif ord(i) >= 87 and ord(i) <= 90:
        temp += 10
print(temp)
    