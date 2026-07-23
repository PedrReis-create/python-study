# Some apenas os números pares entre 1 e 200.

soma = 0

for numero in range(1, 201):
    if numero % 2 == 0:
        soma += numero
    else:
        continue
    
print(soma)