# Conte quantas letras existem na palavra digitada pelo usuário (sem usar len()).

palavra = input('Digite uma palavra: ')
quantidade = 0

for letra in palavra:
    if letra:
        quantidade += 1
    else:
        continue
print(f'A sua palavra tem {quantidade} letras')