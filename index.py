import math
numero = float(input("Introduce un número para calcular su logaritmo natural: "))
if numero > 0:
    logaritmo = math.log(numero)
    print("El logaritmo natural es:" + logaritmo)
else:
    print("El número debe ser mayor que cero para calcular el logaritmo natural.")
