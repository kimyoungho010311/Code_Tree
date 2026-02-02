A, B = map(int, input().split())
arr = [0] * B
result = 0

while A > 1:
    arr[A % B] += 1
    A //= B

for cnt in arr:
    result += cnt * cnt

print(result)