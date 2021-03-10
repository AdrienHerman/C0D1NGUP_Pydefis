square = res = 0

for i in range(50):
    square = (i + 1) ** 2
    
    if square % 3 == 0:
        res += square

print(res)
