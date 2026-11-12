numbers = [2, 4, 5, 8, 10, 12, 14]

start = 0
end = len(numbers) - 1
# // it floor division and it gives us integers instead of floats

new_numbers = [3, 6, 9, 12, 15, 18, 21]
target = 15
low = 0
high = len(numbers) -1

while low <= high:
    mid = (low + high) // 2 

    if numbers[mid] == target:
        print("Target found at index: ", mid)
        break
        
    elif numbers[mid] < target:
        low = mid + 1

    else: 
        high = mid - 1

else: 
    print("Target not found")

