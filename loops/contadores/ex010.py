# Calcule o fatorial de um número usando for.
# fatorial = 5! = 5x4x3x2x1

fatorial = int(input('Digite um número para calcular seu fatorial: '))
resultado = 1

for numero in range(1, fatorial+1):
    resultado *= numero
    
print(resultado)