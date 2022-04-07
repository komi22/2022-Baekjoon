while True:
    number_list=list(map(int,input().split()))
    if number_list[0]==0 and number_list[1]==0:
        break
    print(number_list[0]+number_list[1])
