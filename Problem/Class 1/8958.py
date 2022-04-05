number_of_case=input()
test_case_list=[]
for number in range(1,int(number_of_case)+1):
    test_case=input()
    test_case_list.append(test_case)
for test_case_temp in test_case_list:
    temp_count=0
    overall_count=0
    for alp in test_case_temp:
        if alp=='O':
            temp_count+=1
        elif alp=='X':
            temp_count=0
        overall_count+=temp_count
    print(overall_count)
