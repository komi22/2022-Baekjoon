# range(1, 10) = 1~9까지의 숫자 
# range(10) = 0~9까지의 숫자

a = int(input())
b = int(input())
c = int(input())

q = list(str(a * b * c)) #list안에 있는 숫자를 str을 이용하여 문자로 변환
                         # 문자를 숫자로 변환하려면 map(int) 사용
for i in range(10):   # range()함수의 결과는 반복 가능하기 때문에 for 문을 사용해 출력 가능하다.

    print(q.count(str(i))) 
