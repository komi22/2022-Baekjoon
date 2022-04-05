number_list=[]
for i in range(0,10):
    input_number=input()
    number_list.append(int(input_number)%42)
number_list.sort()
count=1
for j in range (0,9):
    if not number_list[j]==number_list[j+1]:
        count+=1
print(count)
