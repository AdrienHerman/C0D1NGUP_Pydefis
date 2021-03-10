from defisurl import DefisUrl

d = DefisUrl("https://pydefis.callicode.fr/defis/ExempleURL/get/IDLEMan/7fd83")
lignes = d.get()

print("\n".join(lignes))

res = int(lignes[0]) + int(lignes[1])

print(res)
rep = d.post(res)
print(rep)
