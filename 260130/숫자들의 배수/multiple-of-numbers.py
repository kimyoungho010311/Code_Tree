N = int(input())
mul_num = 2
idx = 0
cnt = 0
arr = [N]

while True:
    tmp = arr[idx] * mul_num
    mul_num += 1

    arr.append(tmp)

    if tmp % 5 == 0:
        cnt += 1
        if cnt == 2:
            break


for elem in arr:
    print(elem, end=' ')