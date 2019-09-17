# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]

sousTab = None
maxVal = 0
posN = None
posM = None

for i in range(0, len(tab)):
    sousTab = tab[i]
    for j in range(0, len(sousTab)):
        if maxVal < sousTab[j]:
            maxVal = sousTab[j]
            posM = j
            posN = i

print("La valeur maximum est :", maxVal, "et elle se trouve à l'indice [", posN, "][",posM,"]")

