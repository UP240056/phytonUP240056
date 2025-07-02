it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Ej. 1 

print(len(age))
print(max(age))
print(min(age))

#Ej. 2

print("Las listas son conjuntos de datos, y este conjunto puede ser modificado en el momento que queramos, los tuples son conjuntos de datos que no podemos cambiar o modifica; los sets son como las listas, pero los datos no están ordenados, y por último, los diccionarios son como los tuples, pero los datos tampoco están ordenados (como en los sets)")

# Ej. 3

phrase = "I am a teacher and I love to inspire and teach people"
splitphrase = phrase.split()
uniquewords = set(phrase)

print(len(uniquewords))

