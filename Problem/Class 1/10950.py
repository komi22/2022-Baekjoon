input_number=input()
couple_number_list=[]
for i in range(0,int(input_number)):
    couple_number=list(map(int,input().split()))
    couple_number_list.append(couple_number)
for j in couple_number_list:
    print(j[0]+j[1])
