# 공백구분 문제
import sys
inputTemp = list(sys.stdin.readline().rstrip().split(' '))

if inputTemp[0] == '' or inputTemp[0] == ' ':
    del inputTemp[0]
elif inputTemp[-1]== ' ':
    del inputTemp[-1]
print(len(inputTemp))