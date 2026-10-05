arr = [8, 3, 6, 1, 5]

smallest = arr[0]

for i in range(1, len(arr)):
    if arr[i] < smallest:
        smallest = arr[i]

print(smallest)