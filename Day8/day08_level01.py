
# Ej. 1

dog = {}
print(dog)

# Ej. 2

print('Ejercicio 2')

dog ['Name'] = 'Nala'
dog ['Color'] = 'Beige'
dog ['Breed'] = 'Labrador'
dog ['Legs'] = '4'
dog ['Age'] = '14'

print(dog)

# Ej. 3

student = {
'First name': 'José Luis',
'Last name': 'Rangel Zayas',
'Gender': 'male',
'Age': '18',
'Material Status': 'Single',
'Skills': ['Good at hardware','B2 in english','Senior Data Analyst'],
'Address': {'State':'Sinaloa', 'City': 'Mazatlán'}
}

print(student)

# Ej. 4

print(len(student))

# Ej. 5

print(student.get('Skills'))

# Ej. 6

student['Skills'].extend(['Good atFrontend', 'Creative'])
print(student)

# Ej. 7

studntkeys = student.keys()
print(studntkeys)

# Ej. 8

studentvalues = student.values()
print(studentvalues)

# Ej. 9

studentlist = student.items()
print(studentlist)

# Ej. 10

del student['Age']
print(student)

# Ej. 11

del dog
