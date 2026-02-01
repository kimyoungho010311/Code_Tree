in_arr = list(map(int, input().split()))
out_arr = []

# 배열을 입력받다 마지막 원소가 0임을 체크
if in_arr[-1] == 0:
    in_arr.pop()

for elem in in_arr:
    if elem % 2 != 0:
        elem += 3
        out_arr.append(elem)

    elif elem % 2 == 0:
        out_arr.append(int(elem / 2))


for elem in out_arr:
    print(elem ,end=' ')