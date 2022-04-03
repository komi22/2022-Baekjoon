#OX퀴즈 (8958)

n = int(input())
fs = 0; total = 0; final = []

for count in range(n):
    r_list = list(input())

    for res in r_list:
        if ( res == 'O'):
            fs += 1
            total += fs
        elif ( res == 'X'):
            fs = 0
    final.append(total)
    total = 0; fs = 0

for cnt_i in final:
    print(cnt_i)
