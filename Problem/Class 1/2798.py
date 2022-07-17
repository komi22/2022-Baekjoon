# 브루트 포스 (완전탐색 알고리즘 즉, 가능한 모든 경우의 수를 모두 탐색하면서 요구조건 충족)
# 100%의 확률로 정답만을 출력한다.

from itertools import permutations # for 문을 사용하지 않고 순열 구할 수 있다.

n, m = map(int, input().split())

num = list(map(int, input().split()))
permutationArray = permutations(num, 3) 
ans = 0
for i in permutationArray:
    if(m+1 > sum(i)):
        ans = max(ans, sum(i))
    
print(ans)