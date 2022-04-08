width_length=list(map(int,input().split()))
length=width_length[0]
width=width_length[1]


chess_board=[]
for i in range(0,length):
    chess_board_line=input()
    chess_board.append(chess_board_line)
#chess board complete

sliced_chess_board=[]
sliced_chess_board_list=[]
for i in range(0,width-7):
    for j in range(0,length-7):
        for k in range(0,8):
            sliced_chess_board.append(chess_board[j+k][i:i+8])
        sliced_chess_board_list.append(sliced_chess_board)
        sliced_chess_board=[]
#complete sliced chess board list

count_list=[]
for test_chess_board in sliced_chess_board_list:
    for i in range (0,2):
        count=0
        for row_number in range(1,9):
            for alp_number in range(1,9):
                w_or_b=(-1)**(row_number+alp_number+i)
                if w_or_b==1:
                    w_or_b='W'
                else:
                    w_or_b='B'
                if not test_chess_board[row_number-1][alp_number-1]==w_or_b:
                    count+=1
        count_list.append(count)
print(min(count_list))
