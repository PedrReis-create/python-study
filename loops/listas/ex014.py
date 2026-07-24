# Contar números pares

numeros = [5, 8, 2, 9, 1, 6, 10]
contador = 0

for numero in numeros:
    if numero % 2 == 0:
        contador += 1
    else:
        continue

print(contador)