import random

def replace_negative(nums):
    for i in range(len(nums)):
        if nums[i] < 0:
            nums[i] = 0
    print("Updated:", *nums)

n = int(input())
numbers = []
for i in range(n):
    numbers.append(random.randint(-100, 100))

print("Values:", *numbers)
replace_negative(numbers)