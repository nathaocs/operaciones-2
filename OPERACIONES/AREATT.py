
def area_triangulo(base, altura):
    area = (base * altura) / 2
    return area


base = float(input("base del triangulo: "))
altura = float(input("altura del triangulo: "))

area = area_triangulo(base, altura)
print(f"area triangulo es: {area}")
