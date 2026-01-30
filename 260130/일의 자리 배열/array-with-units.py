N, M = map(int, input().split())
arr = [N, M]

for i in range(2, 10):
    tmp = (arr[i-2] + arr[i-1]) % 10
    arr.append(tmp)

for elem in arr:
    print(elem, end=" ")