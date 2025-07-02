it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Ej. 1

A.update(B)

# Ej. 2

print(B.intersection(A))

# Ej. 3

print(A.issubset(B))

# Ej. 4

print(A.isdisjoint(B))

# Ej. 5

A.update(B)
B.update(A)

# Ej. 6

print('Between A and B: ', A.difference(B))
print('Between B and A: ', B.difference(A))

# Ej. 7

del A
del B