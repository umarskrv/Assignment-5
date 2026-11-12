
n = int(input())

months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

month = 1

for days in months:
    if n > days:
        n = n - days
        month = month + 1
    else:
        break

print(n, month)
