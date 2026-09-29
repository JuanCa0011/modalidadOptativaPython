entrada=input("Dime una frase con guiones ")
partes=entrada.split("-")
palabras=len(partes)
for valor in range(palabras):
    print(partes[valor])