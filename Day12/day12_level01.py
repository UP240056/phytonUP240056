# Bases

import random
import string

def random_user_id():
    caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join(random.choice(caracteres) for _ in range(6))

print(random_user_id())  

# Ej. 1

import random
import string

def user_id_gen_by_user():
    num_caracteres = int(input("Número de caracteres por ID: "))
    num_ids = int(input("Número de IDs a generar: "))
    
    caracteres = string.ascii_letters + string.digits
    for _ in range(num_ids):
        print(''.join(random.choice(caracteres) for _ in range(num_caracteres)))

# Ej. 2

import random

def rgb_color_gen():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r},{g},{b})"

print(rgb_color_gen())