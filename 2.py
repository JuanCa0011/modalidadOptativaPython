#Recibe una frase del usuario y muestra: frase sin espacios extremos, en minusculas y numero de caracteres.
# Recibir la frase del usuario
frase = input("Ingresa una frase: ")

# Limpiar espacios extremos y convertir a minúsculas
frase_limpia = frase.strip().lower()

# Mostrar los resultados
print(f"Frase procesada: '{frase_limpia}'")
print(f"Número de caracteres: {len(frase_limpia)}")