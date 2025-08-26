import numpy as np
# Miscellaneous

# Load data from file

data = np. genfromtxt('data.txt', delimiter=',')

print(data.astype('int16')) # transforme uniquement lors du print 

# data = data.astype('int16') # si on veux modifier 


## Advenved indexing

## Boolean Masking and advanced indexing
# ou est-ce que data > 50
print(data>50)

print(data[data>50]) # pour obtenir leur indexs
# on peux faire cela car on peux indexé des variables
a = np.array([1,2,3,4,5,6,7,8,9])
print(a[[1,2,8]]) # Element 1 2 et 8

print(np.any(data > 50, axis=0))
# Cela analyse par colonnes et donne un resultat pour chaque colonne grace au axis
# Sans le axis, cela analyse dans tout le arrays et me dit un true ou false pour tout l'array

print(np.all(data > 50, axis=0))
# Tout les éléments de la colonnes doivent être supérieure à 50 

# Conditions multiples
print("Conditions multiples")
print((data > 50) & (data < 100))
print(~(data > 50) & (data < 100)) # négation


# test 
# test = np.array([0], dtype='int8')
arr = np.zeros((30), dtype='int8')
arr[arr.size()-1] = arr[arr.size()-1]-1
print(arr)

# np.reshape(arr, (5,6))

print(np.reshape(arr, (6,5)))