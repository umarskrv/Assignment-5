import random

def get_even(nums):
    evens = []
    for item in nums:
        if item % 2 == 0:
            evens.append(item)
    return evens

def get_odd(nums):
    odds = []
    for item in nums:
        if item % 2 == 1:
            odds.append(item)
    return odds

n = int(input())
numbers = []
for i in range(n):
    numbers.append(random.randint(0, 100))

print("Random array:", *numbers)
evens = get_even(numbers)
odds = get_odd(numbers)
print("Even numbers:", evens, "Length:", len(evens))
print("Odd numbers:", odds, "Length:", len(odds))