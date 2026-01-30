in_arr = list(map(int, input().split()))
out_arr = []
in_arr.pop()

for elem in in_arr:
    if elem % 2 != 0:
        elem += 3
        out_arr.append(elem)
    elif elem % 2 == 0:
        out_arr.append(int(elem / 2))


for elem in out_arr:
    print(elem ,end=' ')