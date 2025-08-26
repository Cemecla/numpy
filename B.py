import numpy as np

a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a.shape)

# chercher un élément spécifique [r,c]
print(a[1,5])
print(a[1,-2]) # Meme chose en partant de la fin de la chaine

# Chercher un rangée spécifique
print(a[1,:])

# Chercher une colonne spécifique
print(a[:,3])

# Plus approfondie [startindex,finalindex,stepsize]
print(a[0, 1:6:2])
print(a[0, 1:-1:2])

# changer un élément
a[1,5] = 20
print(a[1,:])

a[:, 2] = 5
print(a)

a[:,2] = [1,2]
print(a)
#[[ 1  2   1    4  5  6  7]
#[ 8  9    2   11 12 20 14]]

# exemple 3d
b = np.array([
    [[1,2],
     [3,4]],
    [[5,6],
     [7,8]]
    ])
print(b)

# Récupérer des élément
print(b[0,1,1])
print(b[0,1,:])
print(b[0,:,1])

#Remplacement d'éléments
b[0,1,1] = 5
print(b[0,1,:])

b[0,1,:] = [5,6] # DOIT ÉTRE DE LA MÊME DIMENSION
print(b[0,1,:])
