N=input()
word_list=[]
for i in range(0,int(N)):
    word=input()
    word_list.append(word)
word_list.sort()
word_list.sort(key=len)
temp=0
for i in word_list:
    if not temp==i:
        print(i)
        temp=i
