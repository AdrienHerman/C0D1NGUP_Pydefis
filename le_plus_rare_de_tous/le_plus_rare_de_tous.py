file = open("input", "r")
file_read = file.read().split("\n")
file_read.remove('')
file.close()

data = [d.split(",") for d in file_read]
pokemon = {}

for d in data:
    if d[0] in pokemon:
        pokemon.update({d[0]:pokemon.get(d[0])+1})
    else:
        pokemon.update({d[0]:1})

frequence = 100
pokemon_moin_frequent = ""

for values in pokemon.items():
    if values[1] < frequence:
        frequence = values[1]
        pokemon_moin_frequent = values[0]

for d in data:
    if d[0] == pokemon_moin_frequent:
        print(d)
