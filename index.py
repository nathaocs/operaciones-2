import math

c1 = float(input("Ingrese el valor del cateto1: "))
c2 = float(input("Ingrese el valor del cateto2: "))

h = float(math.sqrt(c1**2 + c2**2))
print("La hipotenusa es: {h}")
