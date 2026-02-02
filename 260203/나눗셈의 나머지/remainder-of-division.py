A, B = map(int, input().split())

if B == 1:
    print(A * A)
    exit()

arr = [0] * B
result = 0

while A >= 1:
    arr[A % B] += 1
    A //= B

for cnt in arr:
    result += cnt * cnt

print(result)