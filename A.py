import numpy as np

a = np.array([1,2,3])

b = np.array([[9.0,8.0,7.0],[6.0,5.0,4.0]])

# Dimensions
print(a.ndim)
print(b.ndim)

# Shape
print(a.shape) # une dimension avec 3 attributs
print(b.shape) # deux dimensions avec 3 attributs

# Get Type
print(a.dtype)

# Spécifier le type
c = np.array([1,2,3], dtype='int8')
print(c.dtype)
# connaitre la taille de l'array
print(c.itemsize) # 1 = 1 byte
print(b.itemsize) # 8 = 8 bytes

# Total size
print(a.size * a.itemsize)
print(a.nbytes)
print(b.nbytes)