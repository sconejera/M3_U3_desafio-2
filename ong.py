

# Paso 1: Definir la función para calcular el factorial de un número

def factorial(n):
    # Inicializar una variable para almacenar el resultado del factorial
    resultado = 1
    # Iterar sobre un rango de 1 a n (inclusive) y multiplicar cada número por el resultado acumulado
    for n in range(1, n + 1):
        resultado *= n
    return resultado

        
 # Paso 2: Definir la función para calcular la productoria de una lista de números
def productoria(lista):
    # Inicializar una variable para almacenar el resultado de la productoria
    resultado = 1
    # Iterar sobre cada elemento de la lista y multiplicarlo por el resultado acumulado
    for elemento in lista:
        resultado *= elemento
    # Retornar el resultado de la productoria
    return resultado
    

# Paso 3: Definir una función que maneje los cálculos basada en los parámetros recibidos
def calcular(**parametros):
    # Iterar sobre cada par clave-valor de los parámetros
    for clave, valor in parametros.items():
        # Determinar si la clave indica un cálculo de factorial
        if 'fact' in clave:
            # Completar: Llamar a la función factorial y imprimir el resultado con un mensaje adecuado
            resultado = factorial(valor)
            print(f'El factorial de {valor} es {resultado}')
             # Remover esta línea después de completar la tarea
        # Determinar si la clave indica un cálculo de productoria
        elif 'prod' in clave:
            # Completar: Llamar a la función productoria y imprimir el resultado con un mensaje adecuado
            resultado = productoria(valor)
            print(f'La productoria de {valor} es {resultado}')
            pass  # Remover esta línea después de completar la tarea

# Paso 4: Ejecutar la función calcular con ejemplos de factorial y productoria
# Completar: Llamar a la función calcular con diferentes combinaciones de argumentos para probar su funcionamiento
calcular(fact_1 = 5, prod_1 = [4, 6, 7, 4, 3], fact_2 = 6)

"""
def factorial(numero):
    fact = 1
    for n in range(numero, 0, -1):
        fact *= n
    
    return fact
def productoria(numeros):
    prod = 1
    if not numeros:
        return prod
    for n in numeros:
        prod *= n
    return prod
def calcular(**parametros):
    for clave, valor in parametros.items():
        
        if 'fact' in clave:
            resultado = factorial(valor)
            print(f'El factorial de {valor} es {resultado}')
        
        elif 'prod' in clave:
            resultado = productoria(valor)
            print(f'La productoria de {valor} es {resultado}')
calcular(fact_1 = 5, prod_1 = [4, 6, 7, 4, 3], fact_2 = 6)
calcular(fact_3 = 0, fact_4 = 1, prod_2 = [2, 5, 3, 9], prod_3 = [3, 6, 4, 2, 8])
calcular(prod_5 = [], prod_6 = [2360])"""