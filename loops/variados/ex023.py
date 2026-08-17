quantidade = int(input('Digite uma quantidade de números: '))
maior = 0
segundo_maior = 0

for i in range(quantidade):
    numero = int(input('Digite um número: '))
    if numero > maior:
        segundo_maior = maior
        maior = numero
        
    elif numero > segundo_maior:
        segundo_maior = numero
    else:
        pass
print(maior)
print(segundo_maior)    
