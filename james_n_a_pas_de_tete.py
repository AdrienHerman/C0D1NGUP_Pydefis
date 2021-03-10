code = "MAMMOUTHS" 
semaine = {"MO":1, "TU":2, "W":3, "TH":4, "F":5, "SA":6, "SU":7}
lettres = {"M":0, "O":1, "T":2, "U":3, "W":4, "H":5, "F":6, "S":7, "A":8}
possibilites = [[] for i in range(9)]  # 0:M / ... / 8:A

# Pour MO
for i in range(1, 10):          # M
    for j in range(1, 10):      # O
        if (i * 10 + j) % 1 == 0 and i != j:
            ok = True
            
            for a in range(2, 9):
                if (i * 10 + j) % a == 0:   ok = False
            
            if not i in possibilites[0] and ok: possibilites[0].append(i)
            if not j in possibilites[1] and ok: possibilites[1].append(j)


"""
for items in semaine.items():
    l = items[0]
    
    if len(l) == 2:
        for i in range(1, 10):      # 1e lettre
            for j in range(1, 10):  # 2e lettre
                if (i * 10 + j) % items[1] == 0:
                    ok = True
                    
                    for a in range(items[1]+1, 9):
                        if (i * 10 + j) % a == 0:   ok = False
                    
                    if not i in possibilites[lettres.get(l[0])] and ok:
                        possibilites[lettres.get(l[0])].append(i)
                    if not j in possibilites[lettres.get(l[1])] and ok:
                        possibilites[lettres.get(l[1])].append(j)
    else:
        for i in range(1, 10):
            if i % items[1] == 0 and not i in possibilites[lettres.get(l)]:
                ok = True
                
                for a in range(items[1]+1, 9):
                    if i % a == 0:   ok = False
                
                if ok:  possibilites[lettres.get(l)].append(i)
"""

for c in code:
    print("{0} : {1}".format(c, possibilites[lettres.get(c)]))
