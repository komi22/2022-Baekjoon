import sys

N = int(sys.stdin.readline())
code1_count = 0
code2_count = 0

f = [0]*41
f[1] = 1
f[2] = 1

def fibonacci(n):
    global code2_count
    for i in range(3,n+1):
        code2_count = code2_count + 1
        f[i] = f[i-1] + f[i-2]
    return f[n]


code1_count = fibonacci(N)

print(code1_count, code2_count, end=" ")
