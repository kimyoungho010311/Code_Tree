arr = list(map(int, input().split()))
tmp = []

for elem in arr:
    if elem == 0:
        break

    tmp.append(elem)

sum = tmp[-1] + tmp[-2] + tmp[-3]

print(sum)