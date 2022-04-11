while True:
    input_number=input()
    if input_number=='0':
        break
    length=len(input_number)
    count=0
    for i in range(0,length):
        if not input_number[i]==input_number[length-i-1]:
            print('no')
            break
        count+=1
        if count==length:
            print('yes')
