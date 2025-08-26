import numpy as np

# Organistion d'arrays

before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((2,2,2))
print(after)
# on peux reshape de la shape que le veux tant que l'on respecte le nombre de total
# ex : (2,4) = (2,2,2) = 8

# Vertical Stack
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
# On stacke les deux vecteur l'un sur l'autre
print(np.vstack([v1,v2]))
print(np.vstack([v1,v2,v1,v1]))

# Horizontal stack
h1 = np.ones((2,4) , dtype='int8')
h2 = np.zeros((2,2), dtype='int8')
print(np.hstack([h1,h2]))
