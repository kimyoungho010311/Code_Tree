N = int(input())

arr = list(map(int, input().split()))
even_arr = []

for elem in arr:
    if elem % 2 == 0:
        even_arr.append(elem)

reversed_even_arr = even_arr[::-1]

for elem in reversed_even_arr:
    print(elem, end=" ")