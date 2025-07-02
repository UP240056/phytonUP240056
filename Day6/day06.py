# ----------------------------- LEVEL 1 ---------------------------------------------

# Ej. 1

empty_tuple = tuple()

# Ej. 2

siblings = ('Mónica', 'Karla', 'Adriana', 'Claudia')

# Ej. 3

brothers = ('Gonzálo',)

siblings_and_brothers = siblings + brothers

# Ej. 4

print(len(siblings))

# Ej. 5

fathers = ('Monica Zayas', 'José Luis Rangel')

family_members = siblings + fathers
print(family_members)

# ----------------------------- LEVEL 02 ----------------------------------------------

# Ej. 1

del family_members

# Ej. 2

fruits = ('Apple', 'Banana', 'Orange', 'Mango', 'Strawberry', 'Watermelon')
vegetables = ('Carrot', 'Potato', 'Broccoli', 'Tomato', 'Eggplant')
animal_products = ('Meat', 'Milk', 'Jam', 'Sausage', 'Chesse', 'Eggs')

food_stuff_tp = fruits + vegetables + animal_products

# Ej. 4

print(food_stuff_tp[0:8] + food_stuff_tp[9:])

# Ej. 5

print(food_stuff_tp[3:-3])

# Ej. 6

del food_stuff_tp
print ('Banana' in fruits)

# Ej. 7

nordic_Countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_Countries)
print('Iceland' in nordic_Countries)