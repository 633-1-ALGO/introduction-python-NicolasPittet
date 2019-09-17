# Problème : Etant donné un tableau B de "n" nombres réels, on demande de trier le tableau B avec le tri par insertion
# Données : un tableau B de n nombre réels
# Résultat attendu : Le tableau B trié

B = [2, 6, 8, 5, 4, 12, 98, 34, 1]

for i in range(1, len(B)):
    cle = B[i]
    j = i - 1
    #Tant que j >= 0 et que la clé (valeur du moment) est plus petite que la valeur se trouvant juste avant...
    while (j >= 0) and (cle < B[j]):
        #La valeur du moment = la valeur précédente
        B[j+1] = B[j]
        #On descend la position
        j = j - 1
    B[j+1] = cle
print(B)


