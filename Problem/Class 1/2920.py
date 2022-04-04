scale=list(map(int,input().split()))
num_list=[1,2,3,4,5,6,7,8]
num_list_reverse=[8,7,6,5,4,3,2,1]
if num_list==scale:
    print('ascending')
elif num_list_reverse==scale:
    print('descending')
else:
    print('mixed')
