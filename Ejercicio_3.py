# Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def anioBisiesto():
    anio: int = int(input("Ingrese el año: "))

    if(anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)):
        print(f"¡El año {anio} es bisiesto!")
    else:
        print(f"Lo sentimos. El año {anio} NO es bisiesto!")

anioBisiesto()