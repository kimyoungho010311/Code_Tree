'''
N 입력받음

[1, N] 으로 초기화

while문으로 무한 반복하다가

arr[i] = arr[i-2] + arr[i-1]
if arr[i] > 100:
    break

배열 출력
'''

N = int(input())
arr = [1, N]
idx = 2 # idx 3번부터 배열을 계산한다.

while True:
    tmp = arr[idx-2] + arr[idx-1]
    # print(f"tmp: {tmp}")
    # print(f"idx: {idx}")
    # print("")
    arr.append(tmp)

    idx += 1

    if tmp > 100:
        break

for elem in arr:
    print(elem, end=' ')