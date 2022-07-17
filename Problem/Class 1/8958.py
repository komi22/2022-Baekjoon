import sys

a = int(input())
temp = []

for i in range(a):
	temp.append(sys.stdin.readline().rstrip())   

for i in range(a):
    temp2 = 0 # 퀴즈정답 중첩을 위한 변수
    answer = 0  # 퀴즈정답 결과 변수
    for x in range(len(temp[i])):
        if temp[i][x] == 'O':
            temp2+=1
            answer+=temp2
        elif temp[i][x] == 'X':
            temp2=0
    print(answer)