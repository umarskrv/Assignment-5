def get_average(numbers):
    total = 0
    for item in numbers:
        total += item
    return total / len(numbers)

n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

print("Values:", *numbers)
average = get_average(numbers)
print("Average:", average)

result = []
for item in numbers:
    if item <= average:
        result.append(item)
print(*result)