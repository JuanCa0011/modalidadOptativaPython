#Escribe un programa que clasifique una temperatura como baja (<15), normal (15-25) o alta (>25).
temperatura = int(input("Escribeme la temperatura "))
if temperatura < 15:
    print("baja")
elif temperatura <= 25:
    print("normal")
else: 
    print("alta")