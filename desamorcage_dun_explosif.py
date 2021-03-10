nb = 797114
n = int(str(nb)[3:])
u = int(str(nb)[:3])
print(nb, u, n)

for i in range(n):
    u *= 13
    u %= 1000
    

print(u)
