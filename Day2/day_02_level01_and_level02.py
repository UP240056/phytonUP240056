#Ej. 1
name = "José Luis"
apellido = "Rangel Zayas"
edad = 18
ciudad = "Mazatlán"
print("Datos:")
print(f"Nombre: {type(name)}")
print(f"Apellido: {type(apellido)}")
print(f"Edad: {type(edad)}")
print(f"ciudad: {type(ciudad)}")

#Ej. 2

print("Longitud del name:", len(name))

# Ej. 3 

print("First name longer than last name:", len(name) > len(apellido))
print()

# Ej. 4

num1 = 5
num2 = 4

# Ej. 5-10

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
residuo = num2 % num1
exp = num1 ** num2
floor_division = num1 // num2

print("Total:", suma)
print("Difference:", resta)
print("Product:", multiplicacion)
print("Division:", division)
print("Remainder:", residuo)
print("Exponentiation:", exp)
print("Floor Division:", floor_division)
print()

#Ej. 11–12

R = 30
pi = 3.1416
Perimetro = R*2
area_del_curculo = pi*(R*R)
print(area_del_curculo)
print()
circunferencia_del_circulo = pi*Perimetro
print(circunferencia_del_circulo)
print()

#Ej. 13-14

name = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
pais = input("Ingrese su país: ")
edad = int(input("Ingrese su edad: "))  

print("\nDatos del usuario:")
print(f"Nombre: {name}")
print(f"Apellido: {apellido}")
print(f"País: {pais}")
print(f"Edad: {edad}")