arr = [12, 35, 1, 10, 34, 1]

largest = float('-inf')
second = float('-inf')

for i in range(len(arr)):
    if arr[i] > largest:
        second = largest
        largest = arr[i]
    elif arr[i] > second and arr[i] != largest:
        second = arr[i]
print(second)