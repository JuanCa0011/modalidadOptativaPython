#recibe una etiqueta como 'urgente-red' y conviértela a dos partes: prioridad y categoría.
etiqueta = "urgente-red"
prioridad, categoria = etiqueta.split("-")
print(f"Prioridad: {prioridad}") 
print(f"Categoría: {categoria}")


etiqueta = "urgente-red"
# .split() devuelve una lista (array) con las partes
partes = etiqueta.split("-")
# Accedemos a cada elemento por su índice
prioridad = partes[0]
categoria = partes[1]
print(f"Lista completa: {partes}")
print(f"Prioridad (índice 0): {prioridad}")
print(f"Categoría (índice 1): {categoria}")