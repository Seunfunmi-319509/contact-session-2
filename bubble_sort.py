numbers = [5, 3, 8, 2]

n = len(numbers)

for i in range(n):
    swapped = False
    # print("Pass:", i + 1)
    for j in range(n - i - 1):
        # print(numbers[j], numbers[j+1])
        if numbers[j] > numbers[j+1]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
            swapped = True

    if not swapped:
        break
print(numbers)