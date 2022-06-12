################
# Joaquín Cremer - @JoaquinCremer
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Escribir una función que retorne True cuando un número entero es par y False cuando no lo sea, sin utilizar módulo. (%)
"""
def es_par(num):
    aux = abs(num)
    while aux >= 2:
        aux = aux - 2
    return aux == 0
        
    


def principal():
    num = int(input("Ingrese un numero: "))
    print (es_par(num))


if __name__ == "__main__":
    principal()