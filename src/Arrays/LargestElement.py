arr=[4,5,6,8,9]

largest=arr[0]

for i in range(len(arr)):
    if largest < arr[i] :
        largest=arr[i]
    else:
        largest=arr[0]

print(largest)