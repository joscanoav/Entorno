def calcular_promedio(lista):
    if not lista:
        return None
    return sum(lista) / len(lista)
numeros = [1, 2, 3, 4, 5]
promedio = calcular_promedio(numeros)
print(f"El promedio de la lista {numeros} es: {promedio}")
