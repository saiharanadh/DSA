arr = [10, 20, 30, 40]
target = 30
answer = -1
for i in range(len(arr)):
    if arr[i] == target:
        answer = i
        break
print(answer)