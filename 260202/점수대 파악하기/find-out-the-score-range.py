input_arr = list(map(int, input().split()))
no_zero = []
check = [0 for _ in range(11)]

for elem in input_arr:
    if elem != 0:
        no_zero.append(elem)
    elif elem == 0:
        break

for elem in no_zero:
    if elem > 10:
        check[elem // 10] += 1


for idx in reversed(range(len(check))):
    if idx * 10 == 0:
        break
    print(f"{idx * 10} - {check[idx]}")