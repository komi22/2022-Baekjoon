# 알람 시계 (2884)

hour, min = map(int, (input().split()))

if (min - 45 >= 0):
    min -= 45
else:
    min = (min - 45) + 60
    hour -= 1
    if (hour < 0):
        hour = 23

print(hour, min)
