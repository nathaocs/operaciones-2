import math
b=float(input("ingrese numero"))
base=float(input("ingrese base"))
if b>0 and base>1 and base!=1:
    operacion=math.log(b,base)
    print(operacion)
else:
    print("no se puede realizar logaritmo")
    