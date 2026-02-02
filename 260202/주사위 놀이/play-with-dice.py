arr = list(map(int, input().split()))
check_arr = [0 for _ in range(7)]

for elem in range(10):
    check_arr[arr[elem]] += 1

for i in range(1, 7):
    print(f"{i} - {check_arr[i]}")