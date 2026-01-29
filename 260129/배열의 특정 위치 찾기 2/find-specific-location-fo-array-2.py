arr = list(map(int, input().split()))
odd_sum = sum(arr[::2])
even_sum = sum(arr[1::2])


print(abs(odd_sum - even_sum))