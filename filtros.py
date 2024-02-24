# Paso 1: Importar el módulo sys para usar argumentos de la línea de comandos
import sys

# Obtener el umbral desde los argumentos de la línea de comandos. Convertirlo a float para manejar números con decimales.
umbral = float(sys.argv[1])

# Definir el diccionario de productos con sus precios
precios = {
    'Notebook': 700000,
    'Teclado': 25000,
    'Mouse': 12000,
    'Monitor': 250000,
    'Escritorio': 135000,
    'Tarjeta de Video': 1500000
}

# Paso 2: Definir la función para filtrar los productos
def filtrar_productos(precios, umbral, mayor_que=True):
    filtro = []

    for producto, precio in precios.items():
        if mayor_que:
            if precio > umbral:
                filtro.append(producto)
        else:
            if precio < umbral:
                filtro.append(producto)

    return filtro

# Paso 4: Imprimir los resultados
if len(sys.argv) == 2:
    # Llamar a la función filtrar solo con el umbral, usando el valor por defecto para 'mayor_que'
    productos_filtrados = filtrar_productos(precios, umbral)
    if productos_filtrados:
        print(f"Los productos {'mayores' if mayor_que else 'menores'} al umbral son: {', '.join(productos_filtrados)}")
    else:
        print("Lo sentimos, no es una operación válida.")
else:
    # Verificar si el segundo argumento es 'mayor' o 'menor' y llamar a la función filtrar con el valor adecuado para 'mayor_que'
    operacion = sys.argv[2]
    if operacion in ["mayor", "menor"]:
        productos_filtrados = filtrar_productos(precios, umbral, mayor_que=(operacion == "mayor"))
        if productos_filtrados:
            print(f"Los productos {operacion}es al umbral son: {', '.join(productos_filtrados)}")
        else:
            print("Lo sentimos, no es una operación válida.")
    else:
        print("Uso: python filtro.py <umbral> [mayor/menor]")
