import numpy as np
# Mathématics

a = np.array([1,2,3,4])
print(a)

a += 2
print(a)
# on peux directement faire de l'arythmétique avec les arrays

b = np.array([1,0,1,0], dtype='int8')
print(a+b)
# deux arrays de même taille vont pouvoir faire de l'arythmétique sur les même index

#Obtenir le sinus de chaque élément
print(np.sin(a))

## Algébre linéaire
# Pour faire de l'algèbre linéaire il faut que le nombre de collonnes de la première array soit égale au nombre de rangé de la deuxième array
c = np.ones((2,3), dtype='int8')
print(c)

d = np.full((3,2), 2)
print(d)

print(np.matmul(c,d))

# trouver le déterminant
e = np.identity(3,  dtype='int8')
print(np.linalg.det(e))

# statistiques
stats = np.array([[1,2,3],[4,5,6]])
print(stats)

print(np.min(stats))
print(np.max(stats, axis=0)) # Renvoie le colonne
print(np.sum(stats))
print(np.sum(stats,axis=0)) # fais la somme par colonne
