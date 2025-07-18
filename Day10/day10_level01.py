# Ej. 1

print("0 al 10:")
print("For loop:")
for i in range(11):
    print(i, end=" ")
print("While loop:")
i = 0
while i <= 10:
    print(i, end=" ")
    i += 1

#Ej. 2

print("10 al 0:")
print("For loop:")
for i in range(10, -1, -1):
    print(i, end=" ")
print("While loop:")
i = 10
while i >= 0:
    print(i, end=" ")
    i -= 1

# Ej. 3

print("\n\n3. Triangle pattern:")
for i in range(1, 8):
    print('#' * i)

# Ej. 4
print("\n4. 8x8 grid:")
for i in range(8):
    print('# ' * 8)

# Ej. 5

print("\n5. Multiplication pattern:")
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# Ej. 6

print("\n6. Iterate through list:")
languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in languages:
    print(language)

# Ej. 7

print("\n7. Even numbers 0-100:")
for i in range(0, 101, 2):
    print(i, end=" ")

# Ej. 8

print("\n\n8. Odd numbers 0-100:")
for i in range(1, 101, 2):
    print(i, end=" ")