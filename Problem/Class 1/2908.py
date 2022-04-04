num1, num2=input().split()
for i in range(2,-1,-1):
    if num1[i]>num2[i]:
        winner=num1
        break
    elif num1[i]<num2[i]:
        winner=num2
        break
winner_reverse=""
for j in winner:
    winner_reverse=j+winner_reverse
print(winner_reverse)
