################
# Joaquín Cremer - @JoaquinCremer
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
Implementar una función que obtenga los máximos, mínimos y promedio de una secuencia con números, retornando los valores como una tuple.
"""
def secuenciador(numero):
    contador_numeros = 0
    cantidad_numeros = int(input("Ingrese la cantidad de numeros a analizar: "))
    numero = int(input("Ingrese un numero: "))
    secuencia = list(numero)
    while contador_numeros <= cantidad_numeros:
        numero = int(input("Ingrese otro numero: "))
        secuencia = secuencia.append(numero)
        contador_numeros = contador_numeros + 1
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
#def promedio(secuencia):
    
        
        
def principal():
    secuencia = 1,5,60,7,700
    resultado = maximo(secuencia), minimo(secuencia) 
    print(resultado)
    

if __name__ == "__main__":
    principal()
