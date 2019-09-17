# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."


print("Il y a", texte.count("exemple"), "fois le mot 'exemple' dans le texte")
print(texte.replace("est", "représente"))

print(texte[::-1])
