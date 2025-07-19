import random

# Ej. 1

def list_of_hexa_colors(num_colors=1):

    colors = []
    hex_chars = '0123456789abcdef'
    
    for _ in range(num_colors):
        color = '#'
        for _ in range(6):
            color += random.choice(hex_chars)
        colors.append(color)
    
    return colors

# Ej. 2

def list_of_rgb_colors(num_colors=1):

    colors = []
    
    for _ in range(num_colors):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        colors.append(f'rgb({r}, {g}, {b})')
    
    return colors

# Ej. 3

def generate_colors(color_type, num_colors):

    if color_type.lower() == 'hexa':
        return list_of_hexa_colors(num_colors)
    elif color_type.lower() == 'rgb':
        return list_of_rgb_colors(num_colors)
    else:
        raise ValueError("El tipo de color debe ser 'hexa' o 'rgb'")