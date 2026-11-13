def get_max(nums):
    biggest = nums[0]
    for item in nums:
        if item > biggest:
            biggest = item
    return biggest

def get_min(nums):
    smallest = nums[0]
    for item in nums:
        if item < smallest:
            smallest = item
    return smallest

n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

print("Values:", *numbers)
print("Minimum:", get_min(numbers))
print("Maximum:", get_max(numbers))