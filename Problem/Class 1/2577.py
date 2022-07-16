a = int(input())
b = int(input())
c = int(input())

temp = str(a*b*c)
for x in range(10):
    answer = 0
    for i in range(len(temp)):
        if x==int(temp[i]):
            answer+=1
    print(answer)