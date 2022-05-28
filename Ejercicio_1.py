# Escribe una función que calcule el área de un triángulo,
# recibiendo la altura y la base como parámetros
# y otra función que calcule el área de un círculo recibiendo el radio del mismo.


def areaTriangulo(base, altura):
    area = (base * altura) / 2
    return area





def areaCirculo(radio):
    area = 3.14 * (radio * radio)
    return area


triangulo = areaTriangulo(5, 10)
print('El area del Triangulo es: ', triangulo)

print('---------------------------------------')

circulo = areaCirculo(10)
print('El area del circulo es: ', circulo)
