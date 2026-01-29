arr = list(map(int, input().split()))

reversed_arr = arr[::-1]

if reversed_arr[0] == 0:
    reversed_arr.remove(0)

for i in reversed_arr:
    print(i, end=' ')