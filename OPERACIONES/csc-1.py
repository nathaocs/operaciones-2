import math

def funcioncosecanteala1(x):
    if abs(x) < 1:
        return "Cosecante a la -1 solo está definida para |x| ≥ 1"
    else:
        angulo = math.asin(1 / x)
        return f"csc⁻¹({x}) = {angulo} radianes"

entrada = float(input("Entrada: "))
resultado = funcioncosecanteala1(entrada)
print(resultado)
