def is_sorted(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i - 1]:
            return False
    return True

n = int(input())
numbers = list(map(int, input().split()))

if is_sorted(numbers):
    print("The array is sorted")
else:
    print("The array is not sorted")