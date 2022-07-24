import sys

k,n = map(int,sys.stdin.readline().split())

result = []

for i in range(k):
    result.append(int(sys.stdin.readline()))

start = 1
end = max(result)

while start <= end:
    mid = (start + end) //2
    count = 0

    for i in range(k):
        count += result[i] // mid
    if count >= n:
        start = mid +1
    else:
        end = mid-1
print(end)
