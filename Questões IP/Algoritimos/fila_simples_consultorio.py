FILA_MAX = 5
FILA_ATUAL = 0

fila = []

def cadastrar_paciente():
    global FILA_ATUAL
    if FILA_ATUAL < FILA_MAX:
        global fila #permitir que fila seja alterada
        nome = input("Digite o nome do paciente: ")
        fila.append(nome)
        FILA_ATUAL += 1
        print("%s foi cadastrado com sucesso na posição %d da fila."
                    % (nome, FILA_ATUAL))
    else:
        print("A fila está cheia. Paciente não foi cadastrado.")
    
    print("\n")
    
def atender_paciente():
    global FILA_ATUAL
    
    if FILA_ATUAL > 0:
        global fila
        
        nome = fila.pop(0)
        FILA_ATUAL -= 1
        
        print("O paciente %s foi atendido." % nome)
         
    else:
        print("Não tem nenhum paciente na fila. Ninguém foi atendido.")
    
    print("\n")

def mostrar_fila():
    print(" ==== MOSTRAR FILA ==== ")
    if FILA_ATUAL > 0:
        for i, paciente in enumerate(fila):
            print(" [%d] - %s" % (i+1, paciente))
    else:
        print(" A fila está vazia.")
    
    print("\n")

while True:
    print(" 1 - Cadastrar paciente na fila")
    print(" 2 - Atender paciente da fila")
    print(" 3 - Mostrar fila")
    print(" 4 - Sair")
    opcao = int(input("> "))
    
    if opcao < 1 or opcao > 4:
        print("Opção inválida, por favor, tente novamente!")
        continue
    elif opcao == 1:
        cadastrar_paciente()
    elif opcao == 2:
        atender_paciente()
    elif opcao == 3:
        mostrar_fila()
    elif opcao == 4:
        print("Saindo do programa")
        break
