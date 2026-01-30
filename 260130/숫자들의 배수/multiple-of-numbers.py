N = int(input())

arr = [N, 0, 0, 0, 0, 0, 0, 0, 0, 0] # size: 10
answer = []
cnt = 0

for idx in range(1, 10):
    arr[idx] = N * (idx+1)


for elem in arr:
    print(elem, end=' ')
    if arr[idx] % 5 == 0:
        cnt += 1

    if cnt >= 2:
        #print(arr[:idx+1])
        arr = arr[:idx+1]
        break