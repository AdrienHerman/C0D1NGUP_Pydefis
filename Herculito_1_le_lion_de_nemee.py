alpha = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")
liste = "ARTEMIS ASCLEPIOS ATHENA ATLAS CHARON CHIRON CRONOS DEMETER EOS ERIS EROS GAIA HADES HECATE HEPHAISTOS HERA HERMES HESTIA HYGIE LETO MAIA METIS MNEMOSYNE NYX OCEANOS OURANOS PAN PERSEPHONE POSEIDON RHADAMANTHE SELENE THEMIS THETIS TRITON ZEUS".split(" ")
liste_nb = [0 for i in range(len(liste))]

for i in range(len(liste)):
    for lettre in liste[i]:
        liste_nb[i] += alpha.index(lettre) + 1

def permuter(tab, i, j):
    temp = tab[i]
    tab[i] = tab[j]
    tab[j] = temp
    
    return tab

for i in range(len(liste)):
    for j in range(i+1, len(liste)):
        if liste_nb[i] > liste_nb[j]:
            liste = permuter(liste, i, j)
            liste_nb = permuter(liste_nb, i, j)

for case in liste: print(case, end=" ")
print()
