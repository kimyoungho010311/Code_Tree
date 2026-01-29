arr = list(map(int, input().split()))

even_sum = sum(arr[1::2])
avg = sum(arr[2::3]) / len(arr[2::3])


print(f"{even_sum} {avg:.1f}")