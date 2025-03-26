import math

def factorial(n):
    if n < 0:
        return "El factorial no está definido para números negativos."
    else:
        return math.factorial(n)

numero = int(input("Introduce un número para calcular su factorial: "))
print("El factorial de", numero, "es:", factorial(numero)) 
