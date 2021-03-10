file  = open("input", "r")
file_read = file.read().split("\n")
file_read.remove('')
file.close()

data = [d.split(" ") for d in file_read]

for coord in data:
    isCorrect = True
    for l in coord:
        sum = 0
        for c in l:
            if c.isdigit():
                sum += int(c)
        
        if sum % 13 != 0:
            isCorrect = False

    if isCorrect:
        print(coord[0], coord[1])
