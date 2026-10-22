from database import cadastrar_tarefa, listar_tarefas

def adicionar_tarefa():
    titulo = input("Digite a tarefa que deseja adicionar: ").strip()

    if not titulo:
        print("O título não pode ficar vazio.")
        return
    
    resultado = cadastrar_tarefa(titulo)
    
    if resultado is True:
        print("Tarefa adicionada com sucesso!")
    
    elif resultado is False:
        print("Essa tarefa já existe!")
    
    else:
        print(resultado)


def mostrar_tarefas():
    tarefas = listar_tarefas()

    if tarefas is None:
        print("Erro ao consultar as tarefas.")
        return

    if not tarefas:
        print("Você ainda não tem tarefas cadastradas.")
        return

    print("\nSuas tarefas:")

    for tarefa in tarefas:
        print(f"- {tarefa[1]}")


def mostrar_menu():
    print("\n===== GERENCIADOR DE TAREFAS =====")
    print("1 - Adicionar tarefa")
    print("2 - Ver tarefas")
    print("3 - Sair")

def menu_sistema():
    while True:
        mostrar_menu()

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_tarefa()

        elif escolha == "2":
            mostrar_tarefas()

        elif escolha == "3":
            print("Obrigado por usar o nosso sistema!")
            break

        else:
            print("Opção inválida. Tente novamente.")

    print("Programa encerrado.")

menu_sistema()

