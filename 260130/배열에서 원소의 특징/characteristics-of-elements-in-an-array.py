arr = list(map(int, input().split()))

for idx in range(len(arr)):
    if arr[idx] % 3 == 0:
        print(arr[idx-1])
        break