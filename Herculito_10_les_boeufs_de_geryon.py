
for i in range(1000):
    for j in range(1000):
        for a in range(1000):
            if (i*j*a)/777 == (i+j+a) and i < j < a and (i+j+a) < 1000:
                print(i+j+a)
