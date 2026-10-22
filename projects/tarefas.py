import sys

tarefas = []
def menu_sistema():
    def adicionar_tarefa(tarefas):
        titulo = input('Digite a tarefa que você deseja adicionar: ')
        if titulo in tarefas:
            pass
        else:
            tarefas.append(titulo)
        return tarefas


    def ver_tarefas(tarefas):
        print(tarefas)

    ##MENU##
    while True:
        def menu():
            escolha = int(input("Deseja adicionar uma tarefa(1), ver suas tarefas(2) ou sair do programa(3)?: "))
            
            if escolha == 1:
                adicionar_tarefa(tarefas)
            if escolha == 2:
                ver_tarefas(tarefas)
            if escolha == 3:
                print("Obrigado por usar o nosso sistema!")
                sys.exit()
            else:
                print("Escolha errada!")
                sys.exit()
    menu()
menu_sistema()