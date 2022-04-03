# 음계 (2920)

# 8개의 숫자로 임의로 받음

scale_list = list(map(int, input().split()))

if scale_list == sorted(scale_list):
    print("ascending")
elif scale_list == sorted(scale_list, reverse = True):
    print("descending")
else:
    print("mixed")
