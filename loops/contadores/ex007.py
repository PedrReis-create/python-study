# Conte quantos números pares existem entre 1 e 100

pares = 0

for numero in range(1, 101):
    if numero % 2 == 0:
        pares += 1
    else: 
        continue
print(pares)