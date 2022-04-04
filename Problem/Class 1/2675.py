number_of_test_case=int(input())
number_list=[]
string_list=[]
for number in range(0,number_of_test_case):
    repeat_number,string=input().split()
    number_list.append(repeat_number)
    string_list.append(string)
length=len(number_list)
for i in range(0,length):
    for j in string_list[i]:
        print(int(number_list[i])*j,end="")
    print("")
