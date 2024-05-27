import random
import string

# Generar 300 líneas de caracteres aleatorios
lines = []
for _ in range(300):
    # Número aleatorio de caracteres por línea, asegurándose de tener al menos 2
    num_chars = random.randint(2, 15)
    # Seleccionar caracteres aleatorios del alfabeto y unirlos con espacios
    line = ' '.join(random.choice(string.ascii_lowercase) for _ in range(num_chars))
    lines.append(line)

# Unir todas las líneas en un solo string para guardar en un archivo
output_text = "\n".join(lines)
print(output_text)
