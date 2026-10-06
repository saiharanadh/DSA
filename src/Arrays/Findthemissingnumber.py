arr = [3, 0, 1]

n = len(arr)

total = n * (n + 1) // 2

for num in arr:
    total -= num

print(total)