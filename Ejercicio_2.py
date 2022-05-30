# Escribe una función que pueda decirte si un número (número entero) es primo o no.

def numeroPrimo():
    numero = int(input('Ingrese un numero: '))

    if numero > 1:
        for i in range(2, int(numero)):
            if (int(numero) % i) == 0:
                print(f'El numero {numero} NO ES PRIMO')
                break
            else:
                print(f'El numero {numero} ES PRIMO')

    else:
        print(f'Ingrese un numero mayor 1 ')


print(numeroPrimo())
