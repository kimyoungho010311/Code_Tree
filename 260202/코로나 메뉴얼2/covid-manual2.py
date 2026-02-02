arr = []
hospi = [0, 0, 0, 0]
for _ in range(3):
    arr.append(list(map(str, input().split())))


for elem in arr:
    if elem[0] == 'Y' and int(elem[1]) >= 37:
        hospi[0] += 1 # A로 보내기
    elif elem[0] == 'N' and int(elem[1]) >= 37:
        hospi[1] += 1 # B로 보내기
    elif elem[0] == 'Y' and int(elem[1]) < 37:
        hospi[2] += 1 # C로 보내기
    else:
        hospi[3] += 1 # D로 보내기

for elem in hospi:
    print(elem, end=' ')

if hospi[0] >= 2:
    print("E")