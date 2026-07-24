# Construindo uma nova lista apenas com números pares

numeros = [5,8,2,9,1,6,10]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        continue
    
print(pares)