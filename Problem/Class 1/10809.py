word=list(input())
alp_list=list('abcdefghijklmnopqrstuvwxyz')
for alp in alp_list:
    try:
        print(word.index(alp),end=' ')
    except:
        print(-1,end=' ')
