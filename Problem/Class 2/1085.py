# 직사각형에서 탈출 (1085)

x, y, w, h = map(int, input().split())
min_list = []

min_list.append(h-y)
min_list.append(w-x)
min_list.append(x)
min_list.append(y)

print(min(min_list))
