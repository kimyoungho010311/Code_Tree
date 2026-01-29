# 3 1 14 0 32 3

arr = list(map(int, input().split()))
cnt = 0

for elem in arr:
    if elem == 0:
        break
    cnt += 1

for i in range(cnt - 1, -1, -1):
    print(arr[i], end=" ")

# range(3-1, -1, -1)
# range(2, -1, -1)

# 3 1 14 0 32 3