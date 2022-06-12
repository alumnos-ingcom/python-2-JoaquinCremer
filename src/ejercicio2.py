################
# Joaquín Cremer - @JoaquinCremer
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una función que obtenga los máximos, mínimos y promedio de una secuencia con números, retornando los valores como una tuple.
"""
def secuenciador(cantidad_numeros):
    """
    Esta función pide al usuario numeros y los transforma en una lista con la secuencia de numeros ingresados
    """
    secuencia = []
    contador = 0
    while contador < cantidad_numeros:
        numero = int(input("Ingrese numero: "))
        secuencia.append(numero)
        contador = contador  + 1
    return secuencia

def maximo(secuencia):
    """
    Esta funcion analiza una secuencia de numeros y devuelve el mayor de ellos
    """
    contador = 0
    maximo = secuencia[0]
    while contador < len(secuencia):
        if secuencia[0 + contador] > maximo:
            maximo = secuencia[0 + contador]
        contador = contador + 1
    return maximo

def minimo(secuencia):
    """
    Esta funcion analiza una secuencia de numeros y devuelve el menor de ellos
    """
    contador = 0
    minimo = secuencia[0]
    while contador < len(secuencia):
        if secuencia[0 + contador] < minimo:
            minimo = secuencia[0 + contador]
        contador = contador + 1
    return minimo
def promedio(secuencia):
    """
    Esta función realiza el promedio de los numeros de la secuencia
    """
    suma_numeros = 0
    contador = 0
    while contador < len(secuencia):
        suma_numeros = suma_numeros + secuencia[0 + contador]
        contador = contador + 1
    promedio = suma_numeros / len(secuencia)
    return promedio
    
        
        
def principal():
    cantidad_numeros = int(input("Ingrese la cantidad de numeros a analizar: "))
    secuencia = secuenciador(cantidad_numeros)
    resultado = maximo(secuencia), minimo(secuencia), promedio(secuencia) 
    print(resultado)
    

if __name__ == "__main__":
    principal()
