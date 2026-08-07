# Você precisa criar uma função chamada contar_letras(texto) que receba uma frase ou palavra e conte quantas vezes cada letra aparece.
# O resultado deve ser um dicionário, onde:
# a chave é a letra;
# o valor é a quantidade de vezes que ela apareceu.

# exemplo "banana" retorna {'b': 1, 'a': 3, 'n': 2}

palavra = input('Digite uma palavra para ser contabilizada: ')

def contar_letras(texto):
    contagem = {}
    
    for letra in texto:
        if letra not in contagem:
            contagem[letra] = 1
        else:
            contagem[letra] += 1
            
    return contagem

resultado = contar_letras(palavra)
print(resultado)
        
        