input_number1=list(map(int,input().split()))
input_number2=list(map(int,input().split()))
for i in input_number2:
    if i<input_number1[1]:
        print(i,end=' ')
