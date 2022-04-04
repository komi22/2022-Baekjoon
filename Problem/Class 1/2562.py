number_list=[]
order_list=[]
for order in range (1,10):
    number=int(input())
    number_list.append(number)
    order_list.append(order)

tmp=number_list.index(max(number_list))
print(number_list[tmp])
print(order_list[tmp])
