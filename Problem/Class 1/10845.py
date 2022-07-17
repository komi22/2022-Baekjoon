import sys
n = int(sys.stdin.readline())

Queue = [0]*10000
findex = 0
lindex = 0

for i in range(n):
    c = sys.stdin.readline()
    if c.startswith("push"):
        cx = int(c[5:-1])
        Queue[lindex] = cx
        lindex = lindex + 1
    elif c == "pop\n":
        if findex == lindex:
            print(-1)
        else:
            print(Queue[findex])
            Queue[findex] = 0
            findex = findex + 1
    elif c == "size\n":
        print(lindex - findex)
    elif c == "empty\n":
        if findex == lindex:
            print(1)
        else:
            print(0)
    elif c == "front\n":
        if findex == lindex:
            print(-1)
        else:
            print(Queue[findex])
    elif c == "back\n":
        if findex == lindex:
            print(-1)
        else:
            print(Queue[lindex-1])
        
