hour, minute=map(int,input().split())
minute_sum=hour*60+minute
minute_sum_modified=minute_sum-45
if minute_sum<45:
    minute_sum_modified_special_case=minute_sum_modified+1440
    print(minute_sum_modified_special_case//60,minute_sum_modified_special_case%60)
else:
    print(minute_sum_modified//60,minute_sum_modified%60)
