print("Hola, ia")
tema = "Cómo te llamas?"
print("Este curso utilizará Python para:", tema)


var1 = "Aprendizaje automático"
var2 = "Procesamiento de lenguaje natural"  
var3 = "Visión por computadora"
print(var1 + ": crear modelos predictivos y analizar datos con scikit-learn.")
print(var2 + ": analizar y comprender texto con NLTK y spaCy.")
print(var3 + ": reconocer imágenes y objetos con OpenCV y PyTorch.")

print(f"Aquí todo en una sola linea: {var1}, {var2}, {var3}")

edad = 18
precio = 12.50
curso = "DAM"
activo = True

print(type(edad))
print(type(precio))
print(type(curso))
print(type(activo))

# Variables para almacenar información de la incidencia
numero_incidencias = 5
tiempo_medio_resolucion = 2.5
categoria = "Tecnología"
incidencia_cerrada = False

#Crea variables para almacenar: numero de incidencias, tiempo medio de resolución, categoría y si la incidencia está cerrada o no. Luego imprime el tipo de cada variable.
incidencias = 10
tiempo_medio = 3.5
categoria_incidencia = "Redes"
cerrada = True

for valor in [incidencias, tiempo_medio, categoria_incidencia, cerrada]:
    print(valor, type(valor)) 

# Corrige este codigo para que calcule correctamente el total: 'precio = 19.95; unidades = 3; total = precio * unidades. Y crealo abajo. Para calcular correctamente el total, primero debemos asegurarnos de que la variable `precio` sea un número (float) en lugar de una cadena (string). Aquí está el código corregido:
precio = "19.95"  # Cambiado de string a float
unidades = 3
total = float(precio) * unidades

print(total) 

nombre = input("Nombre: ")
horas = float(input("Horas de estudio: "))
dias = int(input("Numero de dias: "))

media_horas = horas / dias
print("Hola",nombre)
print("Media diaria:", media_horas)


#pide al usuario minutos empleados en una tarea y conviertelos a horas. Luego imprime el resultado.
minutos = float(input("Minutos empleados en la tarea: "))
print(f"Los minutos empleados en la tarea corresponden a {minutos / 60} horas.") 


#pide al usuario, modulo, nota numerica. Muestra una frase completa con esos datos. 
nombre = input("Introduce el nombre: ")
modulo = input("Introduce el módulo: ")
nota= float(input("Introduce la nota numérica: "))
print(nombre, "ha obtenido una nota de", nota, "en el módulo de", modulo)


#Dame la tabla de multiplicar de un numero ingresado por el usuario.
numero = int(input("Introduce un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

#Pide al alumnado que anticipe la salida antes de ejecutar el programa. Después comparad predicción y resultado. 
tokens_entrada = 1200
tokens_salida = 300
total = tokens_entrada + tokens_salida 
porcentaje_salida = tokens_salida / total * 100

print ("Total:", total)
print("Porcentaje de salida:", porcentaje_salida, "%")

#Calcula el precio final de un servicio con precio base, número de usos y un descuento del 10%
baseprice = float(input("Introduce el precio base: "))
amountofuses = int(input("Introduce la cantidad de usos: "))

finalprice = (baseprice * amountofuses) * 0.90

print(f"El precio final con 10% de descuento es: ${finalprice:.2f}")

#Dado un número de registros, calcula cuántos lotes completos de 32 se pueden formar y cuántos registros sobran.
# Pedir el número de registros al usuario
#registros = int(input("Introduce el número de registros: "))#

# 1. Pide el dato al usuario (entra como texto)
texto_ingresado = input("Introduce el número de registros: ")

# 2. Convierte el texto a número entero
numero_entero = int(texto_ingresado)

# 3. Guarda el valor en la variable final
registros = numero_entero 

lotes = registros // 32
sobrantes = registros % 32 

# Mostrar los resultados
print(f"Lotes completos de 32: {lotes}")
print(f"Registros sobrantes: {sobrantes}")


#ejercicio
mensaje =" Error de conexion"
limpio = mensaje.strip().lower()
palabras = limpio .split()

print(limpio)
print(palabras)
print("El mensaje contiene{len(palabra)} palabra")