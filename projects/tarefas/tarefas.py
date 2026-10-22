from database import cadastrar_tarefa

tarefas = []

def adicionar_tarefa(tarefas):
    titulo = input("Digite a tarefa que deseja adicionar: ")

    if titulo in tarefas:
        print("Essa tarefa já existe.")
    else:
        tarefas.append(titulo)
        print("Tarefa adicionada com sucesso!")

def ver_tarefas(tarefas):
    if not tarefas:
        print("Você ainda não tem tarefas cadastradas.")
    else:
        print("\nSuas tarefas:")
        for tarefa in tarefas:
            print(f"- {tarefa}")

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
            adicionar_tarefa(tarefas)

        elif escolha == "2":
            ver_tarefas(tarefas)

        elif escolha == "3":
            print("Obrigado por usar o nosso sistema!")
            break

        else:
            print("Opção inválida. Tente novamente.")

    print("Programa encerrado.")

menu_sistema()


