# 배열 선언
arr = []
cnt = 0

# 정수 한 개를 입력받아 배열의 첫 인덱스에 저장
n = int(input())
arr.append(n)

# 입력받은 정수의 배수를 배열에 저장
for i in range(1, 10):
	a = arr[i - 1] + arr[0]
	arr.append(a)

# 배열의 원소들을 출력하다가 5의 배수가 2번 나오면 출력을 멈춤
for elem in arr:
	print(elem, end=" ")
	if elem % 5 == 0:
		cnt += 1
	if cnt >= 2:
		break
