A, B = map(int, input().split())
arr = [0] * 10
result = 0

while A >= 1:
    A = A // B
    res = A % B
    arr[res] += 1
    # print(A)

# print(arr) # [1, 0, 2, 2, 0, 0, 0, 0, 0, 0]

for idx in range(len(arr)):

    if arr[idx] != 0:
        result += pow(arr[idx], 2)

print(result)