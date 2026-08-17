historico = {}

while True:
    pokemon = input('Digite um pokemon(ou fim se quiser parar): ')
    
    if pokemon.lower() == 'fim':
        break
    
    if pokemon not in historico:
        historico[pokemon] = 1
    else:
        historico[pokemon] += 1
 
if not historico:
    historico = 'Vazio!'       
print(historico)