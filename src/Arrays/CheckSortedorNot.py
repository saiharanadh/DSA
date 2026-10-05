arr = [1, 2, 2, 4, 5]

sortedarray = True

for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        sorted_array = False
        break

print(sortedarray)