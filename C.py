import numpy as np
# Initialisation d'arrays

# Init tout à zero
a = np.zeros(5)
# init [0,0,0,0,0]
print(a)

# plus complexe (2d)
b = np.zeros((2,3))
# init [[0,0,0],[0,0,0]]
print(b)

# encore plus complexe (3d)
c = np.zeros((2,3,3))
''' init [[[0. 0. 0.],[0. 0. 0.],[0. 0. 0.]]
           [[0. 0. 0.],[0. 0. 0.],[0. 0. 0.]]]
'''
print(c)

# init tout à un
d = np.ones((4,2,2), dtype='int8')
print(d)

# tout nombre <taille et dimension> , le nombre à remplir avec
e = np.full((2,2),99)
print(e)

# un autre tout nombre (on imite la shape de b)
f = np.full_like(b,4 , dtype='int8')
print(f)

# init avec des nombre random décimal
g = np.random.rand(4,2)
print(g)

h = np.random.random_sample(a.shape)
print(h)

# init avec des nombre entiers
i = np.random.randint(7, size=(2,2))
# 7 = 0-7
# si je mets 4,7 = 4-7
print(i)

# init une dimension carré
j = np.identity(5, dtype='int8', like=b)
print(j)

# répétitions
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3, axis=0)
print(r1)

# Test 1
output = np.ones((5,5), dtype='int8')
z = np.zeros((3,3), dtype='int8')
z[1,1] = 9
print(z)
output[1:4,1:4] = z
print(output)

#### Si l'on copy
a1 = np.array([1,2,3], dtype='int8')
print(a1)
b1 = a1

print(a1)
# Nous avons copié l'adresse en mémoire

b1 = a1.copy()
b1[0] = 100
print(b1)