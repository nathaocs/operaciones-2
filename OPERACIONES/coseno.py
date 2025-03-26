import math
grados = float(input("A continuación... ingrese el ángulo en grados: "))
radianes = math.radians(grados)
coseno = math.cos(radianes)
print(f"El coseno de {grados}° es {coseno:.4f}")