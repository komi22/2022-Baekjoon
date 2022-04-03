# 평균 (1546)

sub = int(input())
score = list(map(int, input().split()))
max_score = max(score)

for cnt_i in range(sub):
    score[cnt_i] = score[cnt_i]/max_score*100

print("%.2f" %(sum(score)/sub))

