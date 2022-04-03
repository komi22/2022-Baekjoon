intial_numbers=input().split()
square_number_sum=0
for number in intial_numbers:
    square_number_sum+=int(number)**2
answer=0
while True:
    if square_number_sum<10:
        answer=square_number_sum
        break
    square_number_sum=square_number_sum-10  
print(answer)
    
