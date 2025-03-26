import math 

x = float(input("Entrada: "))

if abs(x) < 1:
    print("Cosecante a la -1 solo está definida para |x| ≥ 1")
else:
    angulo = math.asin(1 / x)
    print(f"csc⁻¹({x}) = {angulo} radianes")
    