x = 997
y = 312
z = 663

while 10*x > y:
    x = (y * z) % 10000
    y = (3 * z) % 10000
    z = (7 * z) % 10000

print(x, y, z)
