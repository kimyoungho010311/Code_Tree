a, b = map(int, input().split())

arr = [a, b, 0, 0, 0, 0, 0, 0, 0, 0]

for idx in range(2, 10):
    arr[idx] = arr[idx-1] + (arr[idx-2]) * 2


for elem in arr:
    print(elem, end=' ')