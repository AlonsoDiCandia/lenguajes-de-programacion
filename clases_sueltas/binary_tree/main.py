import time
import random

from BinaryTree import BinaryTree

# Generar una lista de números aleatorios
size = 1000000
data = random.sample(range(size * 10), size)

# Crear y llenar el árbol binario
bt = BinaryTree()
for num in data:
    bt.insert(num)

# Elemento a buscar
target = random.choice(data)

# Medir el tiempo de búsqueda en la lista
start_time = time.time()
found = target in data
end_time = time.time()
list_search_time = end_time - start_time

# Medir el tiempo de búsqueda en el árbol binario
start_time = time.time()
found = bt.search(target) is not None
end_time = time.time()
bt_search_time = end_time - start_time

print(f"Tiempo de búsqueda en la lista: {list_search_time:.7f} segundos")
print(f"Tiempo de búsqueda en el árbol binario: {bt_search_time:.7f} segundos")
