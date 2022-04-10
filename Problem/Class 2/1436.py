input=input()
count=0
order=0
while True:
    count+=1
    str_count=str(count)
    length=len(str_count)
    for i in range(0,length-2):
        if str_count[i:i+3]=='666':
            order+=1
            break
    if int(input)==order:
        print(count)
        break
