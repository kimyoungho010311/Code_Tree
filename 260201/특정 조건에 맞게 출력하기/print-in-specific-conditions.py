'''정수가 차례로 주어지다가 0이 주어지면 0을 제외하고 그때까지 주어진 정수를 차례로 출력하되
그 수가 홀수이면 3을 더한 값을, 짝수이면 2로 나눈 몫을 출력하는 프로그램을 작성해보세요.'''

in_arr = list(map(int, input().split()))
#
# # 배열을 입력받다 마지막 원소가 0임을 체크
out_arr = []
# if in_arr[-1] == 0:
#     in_arr.pop()
#
# for elem in in_arr:
#     if elem % 2 != 0:
#         elem += 3
#         out_arr.append(elem)
#
#     elif elem % 2 == 0:
#         out_arr.append(int(elem / 2))
#

for elem in in_arr:
    if elem == 0:
        break
    else:
        if elem % 2 != 0:
            elem += 3
            out_arr.append(elem)
        elif elem % 2 == 0:
            out_arr.append(int(elem / 2))


for elem in out_arr:
    print(elem ,end=' ')