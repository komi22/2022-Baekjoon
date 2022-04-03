number_of_subject=int(input())
grade=input().split()
grade_int=[]
for i in grade:
    grade_int.append(int(i))
max_grade=max(grade_int)

grade_modified=[]
for i in grade_int:
    grade_modified.append((i/max_grade)*100)

sum_of_grade=0
for i in grade_modified:
    sum_of_grade=sum_of_grade+i
    
print(sum_of_grade/len(grade_modified))
