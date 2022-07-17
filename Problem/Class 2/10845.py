import sys

n = int(sys.stdin.readline())

answer = []
for i in range(n):
	result = list(sys.stdin.readline().split())
	if result[0] == 'push':
		answer.append(result[1])
	elif result[0] == 'pop':
		if len(answer) != 0:
			print(answer.pop(0))
		else:
			print('-1')
	elif result[0] == 'size':
		print(len(answer))
	elif result[0] == 'empty':
		if len(answer) == 0:
			print('1')
		else:
			print('0')
	elif result[0] == 'front':
		if len(answer) == 0:
			print('-1')
		else:
			print(answer[0])
	elif result[0] == 'back':
		if len(answer) == 0:
			print('-1')
		else:
			print(answer[-1])
    
