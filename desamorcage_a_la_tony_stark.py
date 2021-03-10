nb = 1435
i = 0
res = 0

while i < 1435:
    if i % 3 == 0 or i % 5 == 0:
        res += i
    i += 1

print(res)
