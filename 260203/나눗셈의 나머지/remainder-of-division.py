A, B = map(int, input().split())
arr = [0 for _ in range(11)]
result = 0
N = len(arr)
while A >= 1:
    arr[A % B] += 1
    A = A // B

for idx in range(N):
    if arr[idx] != 0:
        result += pow(arr[idx], 2)

print(result)