number_of_lines=int(input())

for line_number in range(1,number_of_lines+1):
    print(" "*(number_of_lines-line_number)+"*"*line_number)
