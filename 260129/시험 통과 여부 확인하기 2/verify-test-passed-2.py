N = int(input())
cnt = 0

for _ in range(N):

    arr = list(map(int, input().split()))

    avg = sum(arr) / len(arr)

    if avg >= 60:
        cnt += 1
        print("pass")
    else:
        print("fail")

print(cnt)