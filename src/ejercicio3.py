################
# Joaquín Cremer - @JoaquinCremer
# UNRN Andina - Introducción a la Ingenieria en Computación
################

"""
3. Súper-puestos
Desarrollar una función que indique el grado de superposición entre dos listas.
Siendo 0 sin superposición y uno para cada elemento superpuesto.
"""
def superpuestos(lista1, lista2):
    resultado = []
    for letra1 in lista1:
        for letra2 in lista2:
            if letra1 == letra2 and letra1 not in resultado:
                resultado.append(letra1)
    return len(resultado)
                
def principal():
    lista1 = list("metamorfosis")    #input("Ingrese una palabra o frase: "))
    lista2 = list("metame")          #input("Ingrese otra palabra o frase: "))
    print(superpuestos(lista1,lista2))
    
    
if __name__ == "__main__":
    principal()
