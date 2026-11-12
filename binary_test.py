numbers = [4, 8, 12, 16, 20, 24, 28]

target = 8

start = 0
end = len(numbers)-1

while start <= end:
    mid = (start + end) // 2

    if numbers[mid] == target:
        print("Target found at index: ", mid)
        break

    elif numbers[mid] < target:
        start = mid + 1

    else:
        end = mid - 1

else:
    print("Target not found!")