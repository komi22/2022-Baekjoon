x,y,w,h=map(int,input().split())
length_list=[]
length_list.append(w-x)
length_list.append(x)
length_list.append(h-y)
length_list.append(y)
print(min(length_list))
