num = int(input())

arr = list(map(int, input().split()))
check_arr = [0 for _ in range(9)]

for elem in arr:
    check_arr[elem-1] += 1

for elem in check_arr:
    print(elem)