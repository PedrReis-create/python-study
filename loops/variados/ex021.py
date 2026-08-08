alunos = [
    {"nome": "Pedro", "nota": 8},
    {"nome": "Maria", "nota": 10},
    {"nome": "João", "nota": 5},
    {"nome": "Ana", "nota": 7}
]

def aprovados(alunos):
    aprovados = []
    
    for aluno in alunos:
        if aluno['nota'] >= 7:
            aprovados.append(aluno['nome'])
            
    return aprovados

print(aprovados(alunos))