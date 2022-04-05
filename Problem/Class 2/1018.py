# 체스판 다시 칠하기 (1018)

s, g = map(int, input().split())

board = []
count_list = []

# 보드 가져오기
for cnt_i in range(s):
    board.append(list(input())) 

# 경우의 수를 고려한 보드 자르기 인덱싱
for cnt_k in range(s-7):
    # 경우의 수를 고려한 보드 자르기 인덱싱
    for cnt_l in range(g-7):
        tmp_chess = []
        # 세로줄 반복문
        for cnt_i in range(cnt_k, cnt_k+8): 
            tmp_line = []
            # 가로줄 반복문
            for cnt_j in range(cnt_l, cnt_l+8):
                tmp_line.append(board[cnt_i][cnt_j])
            tmp_chess.append(tmp_line)

        check_list = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], 
                      ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

        count = 0
        
        # 원본판과 비교할 정답 1줄을 생성
        if tmp_chess[0][0] == 'B':
            check = check_list[1]
            # 정답줄과 원본줄을 비교하면서 다르면 카운터 +1
            for cnt_i in range(8):
                if (tmp_chess[0][cnt_i] != check[cnt_i]):
                    count += 1 
        else:
            check = check_list[0]
            for cnt_i in range(8):
                if (tmp_chess[0][cnt_i] != check[cnt_i]):
                    count += 1 

        # 원본판 첫 줄을 제외한 나머지 판을 정답줄과 비교
        for cnt_i in range(1, 8):
            # 체스판의 규칙에 따라 이전 줄의 첫번째 색과 다음줄의 첫번째 색이 달라야함
            # 즉 색에 따라 정답줄을 바꿔야함    
            if check[0] == 'B':
                check = check_list[0]
            else:
                check = check_list[1]
            # 원본판과 정답판을 비교하며 다르면 카운터 +1
            for cnt_j in range(8):
                if (tmp_chess[cnt_i][cnt_j] != check[cnt_j]):   
                        count += 1 
                else :
                    if (tmp_chess[cnt_i][cnt_j] != check[cnt_j]):
                        count += 1 

        # 상황을 가정한 경우의 카운터 다음 줄에서 설명
        s_count = 0

        # 만약 원본판의 첫번째 줄의 첫 색이 B 였더라도, W로 가정한 경우도 계산해야함
        if tmp_chess[0][0] == 'B':
            check = check_list[0]
            for cnt_i in range(8):
                if (tmp_chess[0][cnt_i] != check[cnt_i]):
                    s_count += 1 
        else:
            check = check_list[1]
            for cnt_i in range(8):
                if (tmp_chess[0][cnt_i] != check[cnt_i]):
                    s_count += 1

        for cnt_i in range(1, 8):

            if check[0] == 'B':
                check = check_list[0]
            else:
                check = check_list[1]

            for cnt_j in range(8):
                if (tmp_chess[cnt_i][cnt_j] != check[cnt_j]):
                        s_count += 1 
                else :
                    if (tmp_chess[cnt_i][cnt_j] != check[cnt_j]):
                        s_count += 1 

        count_list.append(s_count)
        count_list.append(count)

print(min(count_list))
