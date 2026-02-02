arr = list(map(int, input().split()))
no_zero_arr = []
check_arr = [0 for _ in range(1, 10)]

for elem in arr:
    if elem != 0:
        no_zero_arr.append(elem)
    elif elem == 0:
        break

for elem in no_zero_arr:
    if elem // 10 == 0:
        pass
    elif elem // 10 != 0:
        check_arr[(elem // 10)-1] += 1

for idx in range(1, len(check_arr)+1):
    print(f"{idx} - {check_arr[idx-1]}")