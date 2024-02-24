# Paso 1: Definir la lista de velocidades
velocidad = [
    25, 12, 19, 16, 11, 11, 24, 1,
    14, 14, 16, 10, 6, 23, 13, 25, 4, 19,
    14, 20, 18, 9, 18, 4, 18, 1, 3, 4, 2,
    14, 23, 19, 23, 9, 18, 20, 22, 14, 1,
    10, 5, 23, 3, 5, 9, 5, 3, 12, 20, 5,
    11, 10, 18, 10, 14, 5, 23, 20, 23, 21
]

# Paso 2: Definir una función para calcular el promedio de las velocidades
def promedio(velocidad):
    suma = sum(velocidad)
    cantidad = len(velocidad)
    promedio = suma / cantidad
    return promedio


# Paso 3: Definir una función para filtrar las velocidades superiores al promedio
def filtrar(velocidad):

    # Primero, calculamos el promedio de las velocidades usando la función promedio definida anteriormente.
    valor_promedio = promedio(velocidad)
    # Luego, usamos una comprensión de lista para obtener las posiciones de las velocidades superiores al promedio.
    # La función enumerate() es útil aquí para obtener tanto el índice (posición) como el valor de cada elemento en la lista.
    return [i for i, v in enumerate(velocidad) if v > valor_promedio]

# Paso 4: Imprimir el resultado de la función filtrar
# Esto mostrará las posiciones de las correas transportadoras con velocidades superiores al promedio.
print(filtrar(velocidad))