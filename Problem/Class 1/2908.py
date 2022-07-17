import sys

a, b = map(str,sys.stdin.readline().split())

if int(a[::-1]) < int(b[::-1]):
    print(int(b[::-1]))
    
if int(a[::-1]) > int(b[::-1]):
    print(int(a[::-1]))
    
