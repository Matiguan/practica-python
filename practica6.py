import math
#calcular el area de un circulo
def area_circulo(r):
    area=math.pi*(r*r)
    return area

radio=float(input("ingrese el valor del radio: "))
resultado=area_circulo(radio)
#maneras de concatenar
print("el area del circulo es igual a "+str(resultado))
print(f'con un radio de {radio} el area del circulo es {resultado}')