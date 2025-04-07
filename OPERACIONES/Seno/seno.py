import math
grados = float(input("ingrese el angulo en grados"))
def seno(angulo):
    angulo=math.radians(angulo)
    seno=math.sin(angulo)
    return seno 
print(seno(grados))
